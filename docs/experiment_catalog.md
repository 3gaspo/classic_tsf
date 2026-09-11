# Experiment catalog

## Available preparation

The nine non-PEMS classic panels can be converted into TIME saved-Arrow data
with `scripts/prepare_classic_datasets.py`. This produces data and provenance,
not a forecasting result.

## Planned TimeTensors family

The intended port will reproduce the TimeTensors experiment factors and
baselines on the common classic split/window contract while using TIME storage
and loading. Exact source revisions, model grid, and commands will be recorded
when implementation begins.

## Planned RevIN family

The intended port will reproduce the relevant RevIN normalization comparison
on the same data, horizon, sampling, objective, and seed contract as the
TimeTensors family. Its exact normalization placement and inversion behavior
remain to be selected from the source implementation.

## Planned supervised controls

PatchTST and DLinear are intended first controls. No model, split, horizon, or
training default is currently implemented or implied by the empty catalog
entries.
