import os
import requests
from dotenv import load_dotenv

load_dotenv()

ORS_API_KEY = os.getenv("ORS_API_KEY")


def get_route_stats(coordinates):

    url = "https://api.openrouteservice.org/v2/directions/driving-car"

    body = {
        "coordinates": coordinates
    }

    headers = {
        "Authorization": ORS_API_KEY,
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=body, headers=headers)

    data = response.json()

    summary = data["routes"][0]["summary"]

    distance_km = summary["distance"] / 1000
    duration_min = summary["duration"] / 60

    polyline = data["routes"][0]["geometry"]

    return {
        "distance_km": round(distance_km, 2),
        "duration_minutes": round(duration_min, 1),
        "polyline": polyline
    }
