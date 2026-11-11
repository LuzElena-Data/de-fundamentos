import requests
import logging
import pandas as pd
from pathlib import Path

RAIZ = Path(__file__).parent.parent
RUTA_CSV = RAIZ / "data" / "clima_durango.csv"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename=RAIZ / "clima.log",
)

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

    logging.info(f"Consulta Exitosa ({actual['time']}) Temperatura: {actual['temperature_2m']} {unidades['temperature_2m']} Humedad: {actual['relative_humidity_2m']} {unidades['relative_humidity_2m']} Viento: {actual['wind_speed_10m']} {unidades['wind_speed_10m']}")
    #logging.info(f"Temperatura: {actual['temperature_2m']} {unidades['temperature_2m']}")
    #logging.info(f"Humedad: {actual['relative_humidity_2m']} {unidades['relative_humidity_2m']}")
    #logging.info(f"Viento: {actual['wind_speed_10m']} {unidades['wind_speed_10m']}")

    fila = {
    "fecha": actual["time"],
    "temperatura": actual["temperature_2m"],
    "humedad": actual["relative_humidity_2m"],
    "viento": actual["wind_speed_10m"],
    }

    ya_existe = False
    if RUTA_CSV.exists():
        existentes = pd.read_csv(RUTA_CSV)
        ya_existe = actual["time"] in existentes["fecha"].values

    if ya_existe:
        logging.warning(f"El dato de {actual['time']} ya existe, se omite")
    else:
        df = pd.DataFrame([fila])
        df.to_csv(RUTA_CSV, mode="a", header=not RUTA_CSV.exists(), index=False)
        logging.info(f"Dato de {actual['time']} guardado en el CSV")
    

except requests.exceptions.Timeout:
    logging.error("Error: la API tardo demasiado en responder")
except requests.exceptions.HTTPError:
    logging.error(f"Error: la API respondio con codigo {respuesta.status_code}")



