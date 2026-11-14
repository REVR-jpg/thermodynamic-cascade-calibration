# Thermodynamic Cascade: Wide Binary Calibration

This repository contains the numerical simulation and non-linear regression script used to calibrate the dimensional transition constant ($\Lambda$) for the Thermodynamic Cascade framework.

**Official Zenodo Archive & DOI:** 
[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.23166165-blue.svg)](https://doi.org/10.5281/zenodo.23166165)

This code mathematically isolates the dimensional fracture curve at $\Lambda \approx 0.297$, supplementing the formal white paper: *Empirical Calibration of the Dimensional Transition Constant (Λ) in Scale-Variant Entropic Gravity Using Wide Binary Kinematics*. 

**Files Included:**
* `Cascade_Lambda_Calibration.ipynb` - The primary Python script used to execute the calibration pipeline.
* `12314.jpg` - The resulting scatter plot isolating the transition constant.
Includes microscopic calibration of the Casimir effect modeling fractional dimension scaling (D=2.70285). See the full white paper here: [10.5281/zenodo.24012761]

Read the full white paper on Zenodo: [https://doi.org/10.5281/zenodo](https://doi.org/10.5281/zenodo).[10.5281/zenodo.24012761]
# The Thermodynamic Cascade (v4.0 Master Calibration & Verification Suite)

**Author:** Raymond R. Williams (Mesa, Arizona, USA)  
**Zenodo Archive DOI:** [10.5281/zenodo.23166165](https://doi.org/10.5281/zenodo.23166165)  

## Overview
This repository contains the official Python verification suite and 1,500-pair synthetic ESA Gaia DR3 wide-binary calibration dataset for **The Thermodynamic Cascade: A Unified Fractal Theory of Everything**.

Using non-linear least-squares regression (`scipy.optimize.curve_fit`), the pipeline isolates the universal dimensional transition constant:
$$\Lambda = 0.29715 \pm 0.00172$$

## Files Included
* `thermodynamic_cascade_v4_verification.py`: Self-contained Python script that calibrates $\Lambda$, exports the CSV dataset, computes planetary clock differentials (Earth, ISS, GPS, Mars), verifies the 5 cross-scale proofs ($\alpha^{-1} \approx 137.036$, $m_p/m_e \approx 1836.15$, $a_0 \approx 1.18 \times 10^{-10}\text{ m/s}^2$, $\rho_{\text{vac}}$, and $H_0 = 73.1\text{ km/s/Mpc}$), and generates the 2-panel calibration plot.
* `wide_binary_simulation_data.csv`: 1,500-row wide binary dataset ($2,000\text{ AU} \le r \le 30,000\text{ AU}$).

## Quick Start
```bash
pip install numpy scipy pandas matplotlib
python thermodynamic_cascade_v4_verification.py
