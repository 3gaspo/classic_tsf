# Architecture

Classic TSF inherits the following path unchanged from Classic TIME Template:

```text
classic CSV + config.json
  -> scripts/prepare_classic_datasets.py
  -> shared classic_datasets saved-Arrow tree
  -> timebench.evaluation.Dataset
```

The parent owns conversion, dataset defaults, the classic catalog, TIME
evaluation, metrics, features, and task lifecycle. This child will own the
supervised models, optimization, scientific experiment configurations, Slurm
fronts, result analysis, and reports once they are implemented.

TimeTensors and RevIN source projects are methodological references, not Git
parents. Their scientific paths will be ported into explicitly named external
or proposal packages without importing their data or artifact directories.
All outputs and logs remain scoped to Classic TSF.
