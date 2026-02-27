import mpmath
import pandas as pd
import numpy as np

# 1. High-Precision Setup
mpmath.mp.dps = 25 

def run_simulation(num_obs, e_l_val, entropy_flux=0.10):
    """Core logic engine optimized for grid search."""
    current_s_ent = mpmath.mpf('0.1')
    eta = mpmath.mpf('1.0')
    e_l = mpmath.mpf(str(e_l_val))
    num_obs_mp = mpmath.mpf(str(num_obs))
    
    for i in range(1, 101): # Expanded search to 100 steps
        w_i = eta * current_s_ent * num_obs_mp
        theta = w_i / e_l
        
        if theta >= 1.0:
            return i # Return the step where collapse occurred
            
        # Standard entropy growth
        current_s_ent += (current_s_ent * mpmath.mpf(str(entropy_flux)))
    return 100

def run_grid_search():
    # Define ranges for the search
    observer_range = range(1, 21) # 1 to 20 observers
    logic_tiers = {
        "Low (1.0)": 1.0, 
        "Mid (10.0)": 10.0, 
        "High (50.0)": 50.0, 
        "Functor_Max (250.0)": 250.0
    }
    
    results = []

    print("SEARCHING STABILITY MATRIX...")
    
    for name, e_l_val in logic_tiers.items():
        for obs in observer_range:
            survival_time = run_simulation(obs, e_l_val)
            results.append({
                "Logic_Tier": name,
                "Observers": obs,
                "Survival_Steps": survival_time
            })

    # Convert to Dataframe for analysis
    df = pd.DataFrame(results)
    
    # Identify the Top 3 Stability Peaks
    top_peaks = df.sort_values(by="Survival_Steps", ascending=False).head(3)
    
    print("\n--- STABILITY GRID SEARCH COMPLETE ---")
    print(top_peaks.to_string(index=False))
    
    # Save the full matrix for your HackingPhysics records
    df.to_csv("stability_matrix.csv", index=False)
    print("\nFull matrix saved to: stability_matrix.csv")

if __name__ == "__main__":
    run_grid_search()