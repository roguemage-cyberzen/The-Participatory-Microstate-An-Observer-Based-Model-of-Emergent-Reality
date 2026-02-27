import mpmath
import pandas as pd
import random

# 1. High-Precision Setup
# We use 25 digits of precision for speed, but preserve the mpf objects
mpmath.mp.dps = 25 

def find_quantum_anomalies(total_sims=3000):
    """
    Scans thousands of reality instances to find 'Logic Gaps'—
    regions where quantum states survive despite high environmental stress.
    """
    anomalies = []
    
    print(f"SEARCHING {total_sims} REALITY INSTANCES FOR LOGIC GAPS...")
    print("Parameters: High-Observer Environments (7-12) | Low-Logic Tiers (1-2)")
    print("-" * 65)

    for s in range(total_sims):
        # We focus on High-Stress environments (many observers, low functor agency)
        num_obs = random.randint(7, 12) 
        f_level = mpmath.mpf(random.uniform(1.0, 2.0)) 
        
        current_s_ent = mpmath.mpf('0.1')
        eta = mpmath.mpf('1.0')
        e_l = mpmath.mpf('1.0') * f_level # Observer Logical Agency
        
        # Statistically, high observers/low agency should collapse by Step 5
        # Any survival beyond Step 12 is considered a 'Logic Gap' anomaly
        expected_limit = 5
        
        survived_to = 0
        final_theta = mpmath.mpf('0.0')

        for i in range(1, 21):
            # Calculate Informational Weight (W_I) and Transition Ratio (Theta)
            w_i = eta * current_s_ent * num_obs
            theta = w_i / e_l #
            final_theta = theta
            
            if theta >= 1.0: # Objective Collapse threshold
                survived_to = i
                break
            
            # Simulated fluctuating environmental entropy flux
            # A low roll here represents a 'Quiet Microstate' that allows survival
            current_s_ent += (current_s_ent * mpmath.mpf(random.uniform(0.05, 0.45)))
            survived_to = i

        # ANOMALY DETECTION: Define a survival threshold (e.g., 2.5x the expected limit)
        if survived_to > (expected_limit * 2.5):
            anomalies.append({
                "Anomaly_ID": s,
                "Observers": num_obs,
                "Functor_Level": float(f_level),
                "Steps_Survived": survived_to,
                "Final_Theta": float(final_theta)
            })

    return pd.DataFrame(anomalies)

# --- EXECUTION ---
if __name__ == "__main__":
    anomaly_df = find_quantum_anomalies(3000)
    
    if not anomaly_df.empty:
        print(f"\n[!] LOGIC GAPS FOUND: {len(anomaly_df)} anomalies detected.")
        print("-" * 65)
        # Sorting by 'Steps_Survived' to highlight the most extreme outliers
        print(anomaly_df.sort_values(by='Steps_Survived', ascending=False).to_string(index=False))
        
        print("\nTHEORY ANALYSIS:")
        print("These data points represent 'Gödelian Survivors'.")
        print("Despite high environmental pressure, the local microstate remained")
        print("logically undecidable (Quantum) due to anomalous entropy flux.")
    else:
        print("\nNo anomalies found. The Matrix remains logically consistent and deterministic.")