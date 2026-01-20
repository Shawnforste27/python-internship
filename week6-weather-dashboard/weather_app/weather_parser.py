def parse_weather(data):
    return {
        "city": data["name"],
        "country": data["sys"]["country"],
        "temp_c": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "humidity": data["main"]["humidity"],
        "wind": data["wind"]["speed"],
        "condition": data["weather"][0]["description"]
    }


def c_to_f(temp_c):
    return (temp_c * 9 / 5) + 32
