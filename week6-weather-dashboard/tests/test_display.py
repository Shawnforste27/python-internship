from weather_app.weather_display import show_weather

sample = {
    "city": "Test",
    "country": "TS",
    "temp_c": 10,
    "feels_like": 8,
    "humidity": 70,
    "wind": 15,
    "condition": "clear sky"
}

show_weather(sample)
print("Display test passed")
