
from pathlib import Path

import requests

import pandas as pd  


RAIZ = Path(__file__).parent.parent


url ="https://archive-api.open-meteo.com/v1/archive"

parametros = {
    "latitude": "32.78",
    "longitude": "-96.80",
    "start_date": "2026-11-01",
    "end_date": "2026-11-02",
    "hourly": "temperature_2m",
    "timezone": "UTC",
}

respuesta = requests.get(url, params=parametros, timeout=30)
#print(respuesta.text)
respuesta.raise_for_status()
datos = respuesta.json()


df = pd.DataFrame(datos["hourly"])
df["time"] = pd.to_datetime(df["time"], format="%Y-%m-%dT%H:%M")

df.to_csv(RAIZ / "data" / "clima_historico.csv", index=False)

print(len(df))
print(df.head()) 
print(df.dtypes)
