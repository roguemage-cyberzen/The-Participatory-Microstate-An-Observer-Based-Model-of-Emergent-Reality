import pandas as pd
import numpy as np

def generate_stability_report(input_file="stability_matrix.csv", output_file="Reality_Report.txt"):
    try:
        df = pd.read_csv(input_file)
    except FileNotFoundError:
        print("Error: stability_matrix.csv not found. Run the grid search first.")
        return

    # 1. Identify the 'Global Stability Peak'
    peak = df.loc[df['Survival_Steps'].idxmax()]
    
    # 2. Identify 'High-Stress Survival' (Max steps with > 10 Observers)
    stress_survivors = df[df['Observers'] >= 10]
    high_stress_peak = stress_survivors.loc[stress_survivors['Survival_Steps'].idxmax()]

    # 3. Calculate 'Hackability'
    # Hackability = Gain in survival per unit increase in Logic Level
    # We compare Low vs Functor_Max for 5 observers
    low_obs5 = df[(df['Observers'] == 5) & (df['Logic_Tier'].str.contains("Low"))]['Survival_Steps'].values[0]
    max_obs5 = df[(df['Observers'] == 5) & (df['Logic_Tier'].str.contains("Max"))]['Survival_Steps'].values[0]
    hackability_index = (max_obs5 - low_obs5) / 249.0 # (Delta Stability / Delta Logic)

    # 4. Generate the Report
    report = f"""
================================================================================
          PARTICIPATORY MICROSTATE: REALITY STABILITY REPORT
================================================================================
Generated for: HackingPhysics Project // Core Logic: mpmath 50-dps
--------------------------------------------------------------------------------

[SECTION 1: GLOBAL STABILITY PEAK]
The highest quantum coherence was achieved under the following parameters:
- Logic Tier: {peak['Logic_Tier']}
- Observer Count: {peak['Observers']}
- Max Survival: {peak['Survival_Steps']} steps

[SECTION 2: HIGH-STRESS SURVIVAL]
In environments with consensus (Observers >= 10), stability was maintained by:
- Logic Tier: {high_stress_peak['Logic_Tier']}
- Survival Time: {high_stress_peak['Survival_Steps']} steps
- Note: This represents the "Consensus Threshold" for classical locking.

[SECTION 3: HACKABILITY ANALYSIS]
The "Hackability Index" measures how much a Functor Upgrade impacts reality.
- Current Index: {hackability_index:.4f} steps/LogicUnit
- High Hackability (>0.01): The region is highly responsive to observer intent.
- Low Hackability (<0.01): The region is "hardened" by collective observation.

[SECTION 4: OPERATIONAL RECOMMENDATION]
To maintain an 'Undecidable' (Quantum) state in a classical room, 
utilize {high_stress_peak['Logic_Tier']} functors. 
Avoid regions with Observer counts exceeding {peak['Observers']} without 
a corresponding Functor upgrade.

================================================================================
    """
    
    with open(output_file, "w") as f:
        f.write(report)
    
    print(f"Report successfully generated: {output_file}")
    print(report)

if __name__ == "__main__":
    generate_stability_report()