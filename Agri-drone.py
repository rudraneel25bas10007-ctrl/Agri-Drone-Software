import os

# --- DATA LAYER (File Handling) ---
FILE_NAME = "drone_logs.txt"

def save_log(data):
    with open(FILE_NAME, "a") as f:
        f.write(f"{data['id']}|{data['crop']}|{data['liquid']}|{data['area']}|{data['status']}\n")

def load_logs():
    if not os.path.exists(FILE_NAME):
        return []
    logs = []
    with open(FILE_NAME, "r") as f:
        for line in f:
            parts = line.strip().split("|")
            logs.append({"id": parts[0], "crop": parts[1], "liquid": int(parts[2]), "area": float(parts[3]), "status": parts[4]})
    return logs

# --- BUSINESS LOGIC LAYER (Classification) ---
def classify_efficiency(liquid, area):
    # Logic: Area covered per liter of liquid
    ratio = area / liquid if liquid > 0 else 0
    if liquid < 10:
        return "CRITICAL: REFILL REQUIRED"
    elif ratio > 5.0:
        return "OPTIMAL: High Coverage"
    else:
        return "STANDARD: Normal Flow"

# --- PRESENTATION LAYER (UI/Menu) ---
def main_menu():
    while True:
        print("\n--- AGRI-DRONE SPRINKLER SYSTEM ---")
        print("1. Log New Spraying Session")
        print("2. View Mission History")
        print("3. Delete Log")
        print("4. Summary Stats")
        print("5. Exit")
        
        choice = input("Select an option: ")

        if choice == '1':
            log_id = input("Enter Mission ID: ")
            crop = input("Crop Type (e.g., Wheat, Rice): ")
            liquid = int(input("Liquid Used (Liters): "))
            area = float(input("Area Covered (Acres): "))
            
            status = classify_efficiency(liquid, area)
            log_data = {"id": log_id, "crop": crop, "liquid": liquid, "area": area, "status": status}
            save_log(log_data)
            print(f"Mission Saved. Status: {status}")

        elif choice == '2':
            logs = load_logs()
            print("\nID | Crop | Liquid | Area | Status")
            for l in logs:
                print(f"{l['id']} | {l['crop']} | {l['liquid']}L | {l['area']}ac | {l['status']}")

        elif choice == '4':
            logs = load_logs()
            if logs:
                total_area = sum(l['area'] for l in logs)
                total_liquid = sum(l['liquid'] for l in logs)
                print(f"\nTOTAL PERFORMANCE:")
                print(f"Total Area Covered: {total_area} acres")
                print(f"Total Liquid Dispersed: {total_liquid} Liters")
            else:
                print("No logs found.")

        elif choice == '5':
            break

if __name__ == "__main__":
    main_menu()
