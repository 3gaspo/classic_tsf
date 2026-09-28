# Classic TSF Experiments

Classic TSF is the experiment repository for small supervised forecasting
studies on classic long-term forecasting datasets stored and loaded through
TIME's saved-Arrow format. It derives from the local Classic TIME Template,
which receives reusable benchmark changes transitively from Improved TIME.

The shared dataset scope is Electricity, Traffic, Solar-Energy, Weather,
Exchange Rate, ETTh1, ETTh2, ETTm1, and ETTm2. PEMS is excluded.

## Current status

The inherited conversion and loading path is available through
`scripts/prepare_classic_datasets.py`. TimeTensors- and RevIN-like experiment
ports are planned but not implemented. The supervised split, training-window,
horizon, target-mode, objective, and seed contracts remain to be selected, so
no training command or result is currently claimed. Generic cluster,
artifact-transfer, Seasonal Naive, diagnostics, grid, and reporting helpers
are inherited, but they do not define a runnable classic experiment.
The inherited runtime records explicit cgroup availability and the device
selected by every learned or CPU-only stage; reusable plotting is headless and
uses an external legend for dense comparisons.

Prepare the shared saved-Arrow datasets with:

```bash
PYTHONPATH=src uv run --no-sync python scripts/prepare_classic_datasets.py
```

See the inherited [dataset format](docs/DATASET_FORMAT.md) and
[feature documentation](docs/FEATURES.md) for the reusable data interfaces.
The dataset catalog at `src/timebench/config/datasets.yaml` intentionally has
no split lengths or forecast terms yet.

## Planned experiment layer

This repository will adapt the scientific comparisons from the existing
TimeTensors and RevIN thesis projects while replacing their data materializing
and loading path with the efficient TIME representation. The ports will retain
the source experiment factors and baselines unless an explicit scientific
change is selected. PatchTST, DLinear, and other supervised controls can share
the same approved split and window contract.

## Documentation

- [Architecture](docs/architecture.md) identifies inherited and project-owned
  responsibilities.
- [Experiment catalog](docs/experiment_catalog.md) records implemented setup
  and planned scientific families.
- [Method overview](latex/method_overview.tex) states the intended comparison.
- [Results recap](docs/results_recap.md) records the current evidence boundary.

Generated artifacts use `outputs/dgx/` for DGX/local execution and
`outputs/selena/` after Selena synchronization; runtime records use the
matching `logs/<surface>/` root. Selena jobs write to this project's scratch
`outputs/` and `logs/` roots. Neither tree is shared with a parent or sibling.
Explicit `OUTPUTS_ROOT` and `LOGS_ROOT` overrides are honored. Shared Seasonal artifacts
and logs are the deliberate exception, selected through the inherited
Seasonal path contract and consumed through `TIME_SEASONAL_TASKS_ROOT`.

The inherited lifecycle preserves fully written `computed` task artifacts
across a later outer failure and finalizes them without recomputation; consumers
still require `completed`. Compact dependency references and the shared
finite-context-plus-future validation mask are available when the first classic
forecasting/selection pipeline is implemented.

Inherited experiment artifacts use `<O>/<experiment>/...`, reports use
`<O>/<experiment>/reports/`, and runtime streams, Hydra files, stage logs, and
workflow status stay below `logs/<surface>/<experiment>/`. Run directories use
`manifest.json` as their authoritative scientific configuration and lifecycle
record; launch IDs and timestamps remain in manifests and logs.

The inherited TIME code remains under Apache-2.0. Dataset licenses remain
those of their original providers.
