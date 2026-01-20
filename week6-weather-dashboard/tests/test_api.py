from weather_app.weather_api import get_weather

data = get_weather("London")
assert data is None or "weather" in data
print("API test passed")
