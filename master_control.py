import os
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    print("="*60)
    print("      THE PARTICIPATORY MICROSTATE: MASTER CONTROL OS")
    print("          Logic-First Physics Simulation Suite")
    print("="*60)

def main_menu():
    while True:
        clear_screen()
        print_header()
        print(" [1] LAUNCH REALITY DASHBOARD (Web-Based Visual Lab)")
        print(" [2] RUN UNIVERSAL SIMULATOR (CLI Mode)")
        print(" [3] EXECUTE STABILITY GRID SEARCH (Data Harvesting)")
        print(" [4] GENERATE REALITY STABILITY REPORT (Intelligence)")
        print(" [5] RUN DEEP SEARCH (Anomaly Finder)")
        print(" [6] VIEW PROJECT WHITEPAPER (PDF Info)")
        print(" [Q] SHUTDOWN INTERFACE")
        print("-" * 60)
        
        choice = input("Select Module > ").strip().upper()

        if choice == '1':
            print("\nStarting Streamlit Lab...")
            os.system("streamlit run reality_dashboard.py")
        
        elif choice == '2':
            obs = input("Enter Observer Count: ")
            logic = input("Enter Logic Tier (low/mid/high): ")
            os.system(f"python3 reality_dashboard.py --obs {obs} --logic {logic}")
            input("\nPress Enter to return to menu...")

        elif choice == '3':
            print("\nStarting Grid Search. This may take a moment...")
            os.system("python3 stability_grid_search.py")
            input("\nGrid Search Complete. Press Enter to return...")

        elif choice == '4':
            print("\nProcessing Matrix Data...")
            os.system("python3 generate_report.py")
            input("\nReport Generated. Press Enter to return...")

        elif choice == '5':
            print("\nRunning Deep Search for Logic Gaps...")
            os.system("python3 deep_search_anomalies.py")
            input("\nSearch Complete. Press Enter to return...")

        elif choice == '6':
            print("\nWhitepaper: Participatory_Microstate_Whitepaper.pdf")
            print("Status: Axiomatically Consistent.")
            input("\nPress Enter to return...")

        elif choice == 'Q':
            print("\nShutting down. Reality state: Locked.")
            break
        
        else:
            print("\nInvalid Command. Re-routing...")

if __name__ == "__main__":
    main_menu()