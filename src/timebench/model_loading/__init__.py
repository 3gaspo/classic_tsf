"""Construction and tensor adapters for the classic context-length study."""


def load_forecaster(alias, *, device, context_length, weights=None,
                    horizon=None, channels=None, parameters=None, model_options=None):
    """Load a backbone; supervised parameters remain available through `.model`."""
    if alias == "chronos2":
        from .chronos2 import Forecaster

        return Forecaster(weights, device, context_length)
    if alias in {"patchtst", "dlinear"}:
        from .supervised import Forecaster

        return Forecaster(alias, device=device, context_length=context_length,
                          horizon=horizon, channels=channels,
                          parameters=parameters, model_options=model_options)
    raise ValueError(f"Unsupported model alias: {alias}")
