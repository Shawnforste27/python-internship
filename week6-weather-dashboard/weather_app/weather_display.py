def show_weather(info, unit="C"):
    print("\nCurrent Weather")
    print("----------------")

    temp = info["temp_c"]
    feels = info["feels_like"]

    if unit == "F":
        temp = (temp * 9 / 5) + 32
        feels = (feels * 9 / 5) + 32
        symbol = "°F"
    else:
        symbol = "°C"

    print(f"City: {info['city']}, {info['country']}")
    print(f"Temperature: {round(temp,1)}{symbol}")
    print(f"Feels Like: {round(feels,1)}{symbol}")
    print(f"Condition: {info['condition'].title()}")
    print(f"Humidity: {info['humidity']}%")
    print(f"Wind Speed: {info['wind']} km/h")
