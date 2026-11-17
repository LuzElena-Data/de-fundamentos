import os
from pathlib import Path

import requests
from dotenv import load_dotenv

import pandas as pd   # ← este va arriba, junto a los demás imports


RAIZ = Path(__file__).parent.parent
load_dotenv(RAIZ / ".env")
API_KEY = os.getenv("EIA_API_KEY")

url = "https://api.eia.gov/v2/electricity/rto/region-data/data/"

parametros = {
    "api_key": API_KEY,
    "frequency": "hourly",
    "data[0]": "value",
    "facets[respondent][]": "ERCO",
    "facets[type][]": "D",
    "start": "2026-11-01T00",
    "end": "2026-11-02T23",
    "sort[0][column]": "period",
    "sort[0][direction]": "asc",
}

respuesta = requests.get(url, params=parametros, timeout=30)
respuesta.raise_for_status()
datos = respuesta.json()

filas = datos["response"]["data"]
print(len(filas))
print(filas[0])
print(type(filas[0]["value"]))


limpias = []
rechazadas = []

for fila in filas:
    try:
        limpias.append({
            "fecha": pd.to_datetime(fila["period"], format="%Y-%m-%dT%H"),
            "demanda_mwh": int(fila["value"]),
        })
    except (ValueError, TypeError):
        rechazadas.append(fila["period"])

df = pd.DataFrame(limpias)
df.to_csv(RAIZ / "data" / "demanda_ercot.csv", index=False)

print(f"Validas: {len(limpias)} | Rechazadas: {len(rechazadas)}")
print(df.head())
print(df.dtypes)