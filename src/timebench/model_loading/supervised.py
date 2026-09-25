"""Project tensor adapter around the original PatchTST and DLinear modules.

No fitting, optimization, normalization or checkpoint policy is selected here.
The caller trains `.model`; forecast returns original-scale `(channels, H)`
arrays using the same history orientation as the Chronos-2 adapter.
"""

from types import SimpleNamespace

import numpy as np
import torch


def build_model(alias, *, context_length, horizon, channels, parameters,
                model_options=None):
    """Construct an upstream model with experiment L and task H/channel count."""
    config = SimpleNamespace(**parameters, seq_len=context_length,
                             pred_len=horizon, enc_in=channels)
    if alias == "patchtst":
        from timebench.external_models.patchtst import Model

        return Model(config, **(model_options or {}))
    if alias == "dlinear":
        from timebench.external_models.dlinear import Model

        if model_options:
            raise ValueError("Original DLinear accepts only its configs argument")
        return Model(config)
    raise ValueError(f"Unsupported supervised model alias: {alias}")


class Forecaster:
    supports_covariates = False
    supports_multivariate = True

    def __init__(self, alias, *, device, context_length, horizon, channels,
                 parameters, model_options=None):
        self.alias = alias
        self.device = device
        self.context_length = context_length
        self.horizon = horizon
        self.channels = channels
        self.model = build_model(
            alias, context_length=context_length, horizon=horizon,
            channels=channels, parameters=parameters,
            model_options=model_options,
        ).to(device)

    def forecast(self, histories, horizon, *, past_covariates=None,
                 future_covariates=None):
        for covariates in (past_covariates, future_covariates):
            if covariates is not None and len(covariates):
                raise ValueError(f"{self.alias} does not support covariates")
        if horizon != self.horizon:
            raise ValueError("Supervised model horizon must match its constructed head")
        contexts = []
        for history in histories:
            target = np.asarray(history, dtype=np.float32)
            if target.ndim == 1:
                target = target[None, :]
            if target.ndim != 2 or target.shape[0] != self.channels:
                raise ValueError("History must have shape (channels, time)")
            if target.shape[-1] < self.context_length:
                raise ValueError("History is shorter than experiment context_length")
            contexts.append(target[:, -self.context_length:].T)
        inputs = torch.as_tensor(np.stack(contexts), device=self.device)
        was_training = self.model.training
        self.model.eval()
        try:
            with torch.inference_mode():
                predictions = self.model(inputs).transpose(1, 2).float().cpu().numpy()
        finally:
            self.model.train(was_training)
        if predictions.shape != (len(histories), self.channels, horizon):
            raise ValueError(f"Unexpected {self.alias} prediction shape: {predictions.shape}")
        return list(predictions)
