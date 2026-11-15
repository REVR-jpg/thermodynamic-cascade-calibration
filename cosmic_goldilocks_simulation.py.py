"""
THE COSMIC GOLDILOCKS CASCADE & DARK FOREST SIMULATION SUITE
Author: Raymond Russell Williams (ORCID: 0009-0003-1267-6382)
Related DOIs: 10.5281/zenodo.20810404 | 10.5281/zenodo.23166165
Patent Ref: U.S. Provisional Patent Application No. 63/937,821 (REVR)

Description:
Simulates (1) Subsurface Solar System Habitability Flux (Phi_bio),
(2) Biotic vs. Abiotic Plume Mass-Spectra (Localized Entropy Inversion),
(3) Cosmic Relic Probability across Redshift Filaments (N_cycles), and
(4) Dark Forest Downstream Sink Shadowing vs. REVR Thermodynamic Camouflage.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# =====================================================================
# 1. FUNDAMENTAL CONSTANTS OF THE THERMODYNAMIC CASCADE
# =====================================================================
LAMBDA = 0.29715          # Dimensional Transition Constant (+/- 0.00172)
D_FRACTAL = 3.0 - LAMBDA  # Effective Spatial Dimension = 2.70285
EXP_FLUX = D_FRACTAL - 1  # Fractional Flux Attenuation Exponent = 1.70285
EXP_EVOL = (1.0 - LAMBDA) / 3.0  # Evolutionary Cycle Exponent = 0.234283

# Biological Self-Organization Window (W/m^2) at Subsurface Boundaries
PHI_MIN_ABIOGENESIS = 0.05
PHI_MAX_DESTRUCT = 2.50
PHI_OPTIMAL = 0.85

# =====================================================================
# 2. MODULE 1: SOLAR SYSTEM SUBSURFACE GOLDILOCKS SIMULATOR
# =====================================================================
def simulate_solar_system_targets():
    targets = [
        {"Body": "Earth (Lost City Vents)", "R_AU": 1.00, "Depth_km": 2.5,  "Phi_Internal": 1.25},
        {"Body": "Enceladus (Tiger Stripes)", "R_AU": 9.58, "Depth_km": 37.5, "Phi_Internal": 0.95},
        {"Body": "Europa (Chaos Upwelling)", "R_AU": 5.20, "Depth_km": 50.0, "Phi_Internal": 0.72},
        {"Body": "Titan (Selk Boundary)",    "R_AU": 9.58, "Depth_km": 65.0, "Phi_Internal": 0.24},
        {"Body": "Mars (Deep Aquifer)",      "R_AU": 1.52, "Depth_km": 4.5,  "Phi_Internal": 0.09},
        {"Body": "Ceres (Brine Mantle)",     "R_AU": 2.77, "Depth_km": 50.0, "Phi_Internal": 0.02},
    ]
    df = pd.DataFrame(targets)
    
    # Equation 1 & 3: Fractional Solar Cascade + Tidal/Geothermal Sink Flux
    phi_0_subsurface = 0.05
    df["Phi_Solar_Cascade"] = phi_0_subsurface * (1.0 / df["R_AU"]) ** EXP_FLUX
    df["Phi_Total_W_m2"] = np.round(df["Phi_Solar_Cascade"] + df["Phi_Internal"], 3)
    df["Habitable_Window"] = (df["Phi_Total_W_m2"] >= PHI_MIN_ABIOGENESIS) & (
        df["Phi_Total_W_m2"] <= PHI_MAX_DESTRUCT
    )
    
    # Biosignature Resonance Score (%)
    df["Biosignature_Prob_Pct"] = np.round(
        100.0 * np.exp(-((np.log10(df["Phi_Total_W_m2"]) - np.log10(PHI_OPTIMAL)) ** 2) / (2 * 0.65 ** 2)),
        1
    )
    return df

# =====================================================================
# 3. MODULE 2: COSMIC ARCHAEOLOGICAL RELIC SIMULATOR (EQ. 5)
# =====================================================================
def simulate_cosmic_relic_zones():
    zones = [
        {"Cosmic_Zone": "Inner Core (z=12 JWST CMB Axis)", "Rho_Ratio": 850.0},
        {"Cosmic_Zone": "Dense Filament Node (z=6)",       "Rho_Ratio": 65.0},
        {"Cosmic_Zone": "Inner Galactic Bridge (z=2)",     "Rho_Ratio": 8.0},
        {"Cosmic_Zone": "Milky Way Spiral Arm (z=0)",      "Rho_Ratio": 1.0},
        {"Cosmic_Zone": "Outer Disk Periphery",            "Rho_Ratio": 0.15},
        {"Cosmic_Zone": "Cosmic Under-Dense Void",         "Rho_Ratio": 0.008},
    ]
    df_c = pd.DataFrame(zones)
    df_c["Relative_Evo_Cycles"] = np.round(df_c["Rho_Ratio"] ** EXP_EVOL, 2)
    df_c["Effective_Evo_Age_Gyr"] = np.round(4.0 * df_c["Relative_Evo_Cycles"], 2)
    return df_c

# =====================================================================
# 4. MODULE 3: DARK FOREST SINK SHADOWING VS. REVR CAMOUFLAGE (EQ. 8)
# =====================================================================
def simulate_dark_forest_shadowing():
    r_downstream_ly = np.linspace(1.0, 50.0, 100)
    phi_filament_baseline = 1.0  # Normalized local filament flux
    
    # Case A: Crude Kardashev Type II Harvester (35% efficiency, 65% waste/shadowing)
    p_extract_crude = 0.65
    phi_downstream_crude = phi_filament_baseline - p_extract_crude * (1.0 / r_downstream_ly) ** (EXP_FLUX * 0.35)
    
    # Case B: REVR Resonant Harvester (94.5% efficiency, phase-locked to Lambda = 0.29715)
    p_extract_revr = 0.055
    phi_downstream_revr = phi_filament_baseline - p_extract_revr * (1.0 / r_downstream_ly) ** (EXP_FLUX * 0.35)
    
    return r_downstream_ly, phi_downstream_crude, phi_downstream_revr

# =====================================================================
# 5. EXECUTE & GENERATE PUBLICATION PLOTS
# =====================================================================
if __name__ == "__main__":
    df_solar = simulate_solar_system_targets()
    df_cosmic = simulate_cosmic_relic_zones()
    
    print("\n=== TABLE 1: SOLAR SYSTEM SUBSURFACE GOLDILOCKS TARGETS ===")
    print(df_solar.to_string(index=False))
    
    print("\n=== TABLE 2: COSMIC ARCHAEOLOGICAL RELIC ZONES (EQ. 5) ===")
    print(df_cosmic.to_string(index=False))
    
    # Generate 2x2 Diagnostic Figure for Zenodo Upload
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle(
        "The Cosmic Goldilocks Cascade: Biosignature & Dark Forest Simulation\n"
        f"(Raymond R. Williams, 2026 | Lambda = {LAMBDA}, D = {D_FRACTAL})",
        fontsize=14, fontweight="bold"
    )
    
    # Plot 1: Solar System Subsurface Flux vs. Goldilocks Window
    ax1 = axes[0, 0]
    ax1.barh(df_solar["Body"], df_solar["Phi_Total_W_m2"], color="#1f77b4", edgecolor="black")
    ax1.axvspan(PHI_MIN_ABIOGENESIS, PHI_MAX_DESTRUCT, color="green", alpha=0.18, label="Goldilocks Flux Window")
    ax1.set_xlabel("Subsurface Cascade Flux Phi_total (W/m^2)")
    ax1.set_title("A. Solar System Subsurface Entropy Flux")
    ax1.legend(loc="lower right")
    
    # Plot 2: Abiotic vs. Biotic Plume Mass Spectrum (Enceladus/Europa Detector)
    ax2 = axes[0, 1]
    mass_amu = np.arange(50, 350, 2)
    abiotic_spectrum = np.exp(-mass_amu / 65.0)
    # Biotic cascade shows resonant peaks at C14, C16, C18, C20 lipid/amino scales
    biotic_peaks = np.zeros_like(mass_amu, dtype=float)
    for resonant_mass in [140, 186, 214, 242, 270, 312]:
        biotic_peaks += 0.35 * np.exp(-((mass_amu - resonant_mass) ** 2) / (2 * 3.5 ** 2))
    biotic_spectrum = abiotic_spectrum * 0.6 + biotic_peaks
    ax2.plot(mass_amu, abiotic_spectrum, "--", color="gray", label="Abiotic Plume (Poisson Decay)")
    ax2.plot(mass_amu, biotic_spectrum, "-", color="#d62728", linewidth=2, label="Biotic Cascade (Resonant Spikes)")
    ax2.set_xlabel("Molecular Mass (amu)")
    ax2.set_ylabel("Normalized Abundance")
    ax2.set_title("B. Enceladus/Europa Plume Biosignature Detector")
    ax2.legend()
    
    # Plot 3: Cosmic Relic Evolutionary Maturity (N_cycles)
    ax3 = axes[1, 0]
    ax3.barh(df_cosmic["Cosmic_Zone"], df_cosmic["Effective_Evo_Age_Gyr"], color="#ff7f0e", edgecolor="black")
    ax3.axvline(4.0, color="black", linestyle="--", label="Earth Baseline (4.0 Gyr)")
    ax3.set_xlabel("Effective Evolutionary Maturity (Gyr Equivalent)")
    ax3.set_title("C. Cosmic Archaeological Zone (Relic Probability)")
    ax3.legend()
    
    # Plot 4: Dark Forest Downstream Sink Shadowing vs. REVR Camouflage
    ax4 = axes[1, 1]
    r_ly, cr_flux, revr_flux = simulate_dark_forest_shadowing()
    ax4.plot(r_ly, cr_flux, "-", color="#d62728", linewidth=2.2, label="Crude Harvester (35% Eff. -> Starves Neighbor)")
    ax4.plot(r_ly, revr_flux, "-", color="#2ca02c", linewidth=2.2, label="REVR Camouflage (94.5% Eff. -> Preserves Filament)")
    ax4.axhline(0.75, color="black", linestyle=":", label="Downstream Biosphere Collapse Threshold")
    ax4.set_xlabel("Downstream Distance Along D=2.70285 Filament (Light-Years)")
    ax4.set_ylabel("Remaining Filament Cascade Flux")
    ax4.set_title("D. Dark Forest Sink Shadowing vs. REVR Stealth")
    ax4.legend(loc="lower right")
    
    plt.tight_layout(rect=[0, 0.03, 1, 0.93])
    plt.savefig("cosmic_goldilocks_cascade_simulation.png", dpi=300)
    print("\nSaved high-resolution figure: cosmic_goldilocks_cascade_simulation.png")