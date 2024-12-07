from datetime import datetime
import pytz

def main():
    while True:
        print("\nChoose a region:")
        print("1. Asia\n2. Europe\n3. America\n4. Exit")
        region_choice = input("Select an option (1-4): ")

        if region_choice == "1":
            choose_country("Asia")
        elif region_choice == "2":
            choose_country("Europe")
        elif region_choice == "3":
            choose_country("America")
        elif region_choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 1, 2, 3, or 4.")

def choose_country(region):
    countries = {
        "Asia": {"1": ("Japan", "Asia/Tokyo"), "2": ("China", "Asia/Shanghai"), "3": ("India", "Asia/Kolkata")},
        "Europe": {"1": ("Germany", "Europe/Berlin"), "2": ("England", "Europe/London"), "3": ("Portugal", "Europe/Lisbon")},
        "America": {"1": ("USA", "America/New_York"), "2": ("Canada", "America/Toronto"), "3": ("Mexico", "America/Mexico_City")},
    }
