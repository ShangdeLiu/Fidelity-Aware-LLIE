# Fidelity-Aware-LLIE

Fidelity-Aware Low-Light Image Enhancement for EC601.

## Project Goal

This project investigates whether low-light image enhancement can be accompanied by a useful spatial indicator showing where the enhanced result may deserve additional inspection.

The current prototype enhances a low-light image, computes reference-based enhancement error using paired data, applies controlled input perturbations, and measures output sensitivity.

## Current Prototype

The prototype currently supports:

- Loading paired low-light and normal-light images
- Gamma correction as an initial enhancement baseline
- Reference-error map generation
- Controlled input perturbation
- Output-sensitivity map generation
- Sensitivity/error/brightness correlation analysis
- Visualization of experimental results

The output-sensitivity map is currently an experimental indicator and is **not** treated as a validated reliability measure.

## Dataset

The current prototype uses the paired **LOL low-light dataset**.

The dataset is not included in this repository.

After downloading the dataset, place it in the project directory using the following structure:

    Fidelity-Aware-LLIE/
    ├── LOLdataset/
    │   └── eval15/
    │       ├── low/
    │       └── high/
    ├── test_dataset.py
    └── requirements.txt

## Installation

Install the required Python packages:

    pip3 install -r requirements.txt

## Run

From the repository root directory:

    python3 test_dataset.py

The script will load a paired low-light/reference image, run the initial enhancement and perturbation experiment, display the resulting visualizations, and print correlation measurements.

## Current Status

Completed:
- Dataset loading
- Initial enhancement pipeline
- Reference-error visualization
- Output-sensitivity visualization

In progress:
- Integration of a stronger LLIE baseline
- Evaluation across multiple LOL images
- Validation of the fidelity indicator against reference error
