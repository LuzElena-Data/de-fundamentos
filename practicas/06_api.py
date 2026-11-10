import requests

url = "https://api.open-meteo.com/v1/forecast"

parametros = {
    "latitude": 24.02,
    "longitude": -104.66,
    "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
    "timezone": "America/Mexico_City",
}

try:
    respuesta = requests.get(url, params=parametros, timeout=10)
    respuesta.raise_for_status()
    datos = respuesta.json()

    actual = datos["current"]
    unidades = datos["current_units"]

    print(f"Clima en Durango ({actual['time']})")
    print(f"Temperatura: {actual['temperature_2m']} {unidades['temperature_2m']}")
    print(f"Humedad: {actual['relative_humidity_2m']} {unidades['relative_humidity_2m']}")
    print(f"Viento: {actual['wind_speed_10m']} {unidades['wind_speed_10m']}")

except requests.exceptions.Timeout:
    print("Error: la API tardo demasiado en responder")
except requests.exceptions.HTTPError:
    print(f"Error: la API respondio con codigo {respuesta.status_code}")