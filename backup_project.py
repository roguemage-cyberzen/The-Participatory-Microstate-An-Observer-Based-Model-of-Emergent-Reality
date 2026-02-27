import zipfile
import os
from datetime import datetime

def run_secure_backup():
    # Generate timestamp for the archive name
    timestamp = datetime.now().strftime('%Y%m%d_%H%M')
    zip_name = f"Participatory_Microstate_Archive_{timestamp}.zip"
    
    # Comprehensive file list from the repository
    files_to_bundle = [
        "reality_dashboard.py",         # Visual Lab Suite
        "master_control.py",           # CLI Hub
        "stability_grid_search.py",     # Grid Search Engine
        "deep_search_anomalies.py",     # Anomaly Detector
        "generate_report.py",           # Report Generator
        "The Participatory Microstate.pdf", # Theoretical Whitepaper
        "stability_matrix.csv",         # Research Dataset
        "Reality_Report.txt",           # Generated Report
        "README.md",                    # Project Overview
        "Quick-Start Instructions.md"   # Operator's Manual
    ]
    
    print(f"--- INITIALIZING RESEARCH BACKUP: {zip_name} ---")
    
    success_count = 0
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in files_to_bundle:
            if os.path.exists(file):
                zipf.write(file)
                print(f"✅ SECURED: {file}")
                success_count += 1
            else:
                print(f"❌ MISSING: {file} (Skipping...)")
                
    print("-" * 50)
    if success_count > 0:
        print(f"BACKUP COMPLETE: {success_count} files archived in {zip_name}.")
    else:
        print("ERROR: No files were found to archive.")

if __name__ == "__main__":
    run_secure_backup()
