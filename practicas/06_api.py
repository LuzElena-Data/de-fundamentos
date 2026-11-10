import requests

url = "https://api.open-meteo.com/v1/forecastx"

parametros = {
    "latitude": 24.02,
    "longitude": -104.66,
    "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
    "timezone": "America/Mexico_City",
}

respuesta = requests.get(url, params=parametros, timeout=10)

print(respuesta.status_code)

datos = respuesta.json()
# print(datos["current"]["temperature_2m"])

actual = datos["current"]
unidades = datos["current_units"]


print(f"Clima en Durango: {datos["current"]["time"]}")
print(f"Temperatura: {actual['temperature_2m']} {unidades['temperature_2m']}")  
print(f"Humedad: {actual['relative_humidity_2m']} {unidades['relative_humidity_2m']}")  
print(f"Viento: {actual['wind_speed_10m']} {unidades['wind_speed_10m']}")  