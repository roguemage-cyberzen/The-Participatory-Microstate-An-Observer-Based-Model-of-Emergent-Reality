import streamlit as st
import mpmath
import pandas as pd
import matplotlib.pyplot as plt
import random
import numpy as np
from datetime import datetime

# 1. High-Precision Engine (Foundation: 2026-01-25)
mpmath.mp.dps = 50 

def run_simulation(num_obs, e_l_val, entropy_flux, max_steps=40, dynamic_logic=False):
    current_s_ent = mpmath.mpf('0.1')
    eta = mpmath.mpf('1.0')
    step_size = mpmath.mpf('0.01')
    num_obs_mp = mpmath.mpf(str(num_obs))
    
    results = []
    for i in range(1, max_steps + 1):
        # THE ULTIMATE HACK: Dynamic Scaling
        if dynamic_logic:
            # Scale EL to maintain Theta at exactly 0.95
            current_el = (eta * current_s_ent * num_obs_mp) / mpmath.mpf('0.95')
        else:
            current_el = mpmath.mpf(str(e_l_val))

        w_i = eta * current_s_ent * num_obs_mp
        theta = w_i / current_el
        d_s_ent = current_s_ent * mpmath.mpf(str(entropy_flux))
        
        status = "QUANTUM" if theta < 1.0 else "COLLAPSED"
        results.append({
            "Iteration": i, 
            "Theta": float(theta), 
            "Status": status,
            "Logic_Used": float(current_el)
        })
        
        if theta >= 1.0: break
        current_s_ent += d_s_ent
    return pd.DataFrame(results)

def calculate_min_agency(obs, flux, target_steps=20):
    s_start = mpmath.mpf('0.1')
    s_final = s_start * (mpmath.mpf('1.0') + mpmath.mpf(str(flux)))**(target_steps - 1)
    return float(mpmath.mpf('1.0') * s_final * mpmath.mpf(str(obs)))

# --- UI CONFIGURATION ---
st.set_page_config(page_title="HackingPhysics Master Lab v3.2", layout="wide")
st.title("The Participatory Microstate: Master Research Suite")

tab1, tab2, tab3 = st.tabs(["🔴 Live Lab & Optimization", "🟩 Stability Matrix", "🔍 Anomaly Deep Search"])

# --- TAB 1: LIVE LAB ---
with tab1:
    st.header("Comparative Logic & Active Agency")
    
    with st.sidebar:
        st.subheader("Global Parameters")
        obs = st.slider("Observer Consensus (C_n)", 1, 100, 10)
        flux = st.slider("Entropy Flux Rate", 0.01, 0.50, 0.15)
        
        st.markdown("---")
        st.subheader("🚀 Optimizer Tools")
        target_s = st.number_input("Target Survival Steps", 5, 100, 20)
        min_el = calculate_min_agency(obs, flux, target_s)
        st.info(f"Threshold Agency: {min_el:.4f}")
        
        # ACTIVATE THE HACK HERE
        use_dynamic = st.toggle("Enable Multi-Step Dynamic Logic (The Hack)")
        
        if st.button("Apply Threshold Agency"):
            st.session_state['el_val'] = min_el + 0.01

    # Logic Values
    curr_el = st.session_state.get('el_val', 10.0)
    user_el = st.sidebar.number_input("Current Logical Agency (EL)", 0.1, 5000.0, float(curr_el))
    df_live = run_simulation(obs, user_el, flux, max_steps=target_s+5, dynamic_logic=use_dynamic)

    # --- PLOT FIX (Avoiding LaTeX Errors) ---
    fig1, ax1 = plt.subplots(figsize=(12, 5))
    ax1.plot(df_live['Iteration'], df_live['Theta'], 'b-o', label="Theta (Stress)")
    ax1.axhline(y=1.0, color='r', linestyle='--', label="Collapse Threshold")
    ax1.fill_between(df_live['Iteration'], 0, 1.0, color='green', alpha=0.1)
    
    # Text labels instead of LaTeX to prevent TypeErrors
    ax1.set_title("Reality Consistency Analysis")
    ax1.set_ylabel("Transition Ratio (Theta)")
    ax1.set_xlabel("Logical Steps")
    ax1.legend()
    st.pyplot(fig1)
    
    # METRICS
    m1, m2, m3 = st.columns(3)
    m1.metric("Current State", df_live['Status'].iloc[-1])
    m2.metric("Superposition Steps", len(df_live[df_live['Theta'] < 1.0]))
    m3.metric("Peak Logic Agency", round(df_live['Logic_Used'].max(), 2))

    # REPORT GENERATOR
    st.markdown("---")
    st.subheader("📝 Experiment Log Generator")
    notes = st.text_area("Researcher Notes:", placeholder="Describe the outcome...")
    if st.button("Generate Formal Report"):
        report = f"STAMP: {datetime.now()}\nOBSERVERS: {obs}\nAGENCY: {user_el}\nHACK: {use_dynamic}\nNOTES: {notes}"
        st.download_button("💾 Download Report", report, file_name="reality_log.txt")

# --- TAB 2: HEATMAP (RE-INTEGRATED) ---
with tab2:
    st.header("Phase Map of Objective Consensus")
    if st.button("Generate Matrix"):
        sim_data = []
        for _ in range(300):
            n_obs = random.randint(1, 20)
            l_lvl = random.uniform(1.0, 300.0)
            res = run_simulation(n_obs, l_lvl, 0.15)
            sim_data.append({"Observers": n_obs, "Logic": round(l_lvl, -1), "Survival": len(res)})
        df_mat = pd.DataFrame(sim_data)
        pivot = df_mat.pivot_table(index='Observers', columns='Logic', values='Survival', aggfunc='mean')
        fig2, ax2 = plt.subplots(figsize=(10, 6))
        im = ax2.imshow(pivot, cmap="RdYlGn", origin='lower', aspect='auto')
        plt.colorbar(im, label="Steps to Collapse")
        st.pyplot(fig2)

# --- TAB 3: ANOMALY SEARCH (RE-INTEGRATED) ---
with tab3:
    st.header("Gödelian Gaps & Anomaly Detection")
    if st.button("Run Deep Search"):
        anomalies = []
        for _ in range(500):
            n_o = random.randint(15, 30)
            l_v = random.uniform(1.0, 5.0)
            res = run_simulation(n_o, l_v, random.uniform(0.01, 0.2))
            if len(res) > 12:
                anomalies.append({"Observers": n_o, "Logic": float(l_v), "Survival": len(res)})
        if anomalies:
            df_ano = pd.DataFrame(anomalies)
            fig3, ax3 = plt.subplots()
            ax3.scatter(df_ano['Observers'], df_ano['Survival'], c=df_ano['Logic'], cmap='plasma')
            st.pyplot(fig3)
            st.dataframe(df_ano)