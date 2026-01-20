import requests
import json
import time
import os
from weather_app.config import API_KEY, BASE_URL, CACHE_TIME

CACHE_DIR = "data/cache"
os.makedirs(CACHE_DIR, exist_ok=True)


def _cache_path(city):
    return f"{CACHE_DIR}/{city.lower()}.json"


def get_weather(city):
    cache_file = _cache_path(city)

    # Use cache if valid
    if os.path.exists(cache_file):
        if time.time() - os.path.getmtime(cache_file) < CACHE_TIME:
            with open(cache_file, "r") as f:
                return json.load(f)

    if not API_KEY:
        print("API key not found.")
        return None

    try:
        response = requests.get(
            f"{BASE_URL}/weather",
            params={
                "q": city,
                "appid": API_KEY,
                "units": "metric"
            },
            timeout=10
        )

        if response.status_code == 200:
            data = response.json()
            with open(cache_file, "w") as f:
                json.dump(data, f, indent=4)
            return data
        else:
            print("City not found or API error.")
    except requests.exceptions.RequestException:
        print("Network error.")

    return None
