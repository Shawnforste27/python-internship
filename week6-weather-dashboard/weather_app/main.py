from weather_app.weather_api import get_weather
from weather_app.weather_parser import parse_weather
from weather_app.weather_display import show_weather

def main():
    unit = "C"

    while True:
        print("\nWEATHER DASHBOARD")
        print("1. Search City")
        print("2. Change Unit (C/F)")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            city = input("Enter city name: ").strip()
            data = get_weather(city)

            if data:
                info = parse_weather(data)
                show_weather(info, unit)

        elif choice == "2":
            unit = "F" if unit == "C" else "C"
            print("Temperature unit changed.")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

main()
