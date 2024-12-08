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

    print(f"\nChoose a country in {region}:")
    for Choose, (country, _) in countries[region].items():
        print(f"{Choose}. {country}")

    country_choice = input("Select a country: ")
    if country_choice in countries[region]:
        country_name, timezone = countries[region][country_choice]
        convert_time_to_thailand(country_name, timezone)
    else:
        print("Invalid choice. Please try again.")

def convert_time_to_thailand(country_name, timezone):
    try:
        time_input = input(f"Enter the time in {country_name} (HH:MM): ")
        time_obj = datetime.strptime(time_input, "%H:%M")
        local_tz = pytz.timezone(timezone)
        thailand_tz = pytz.timezone("Asia/Bangkok")
        local_time = local_tz.localize(time_obj)
        thailand_time = local_time.astimezone(thailand_tz)
        print(f"The time in Thailand is: {thailand_time.strftime('%H:%M')}")
    except ValueError:
        print("Invalid time format. Please enter the time in HH:MM format.")