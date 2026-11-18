from pathlib import Path

import pandas as pd

RAIZ = Path(__file__).parent.parent

demanda = pd.read_csv(RAIZ / "data" / "demanda_ercot.csv", parse_dates=["fecha"])
clima = pd.read_csv(RAIZ / "data" / "clima_historico.csv", parse_dates=["time"])

clima = clima.rename(columns={"time": "fecha", "temperature_2m": "temperatura_c"})

unidos = pd.merge(demanda, clima, on="fecha", how="inner")

print(len(unidos))
print(unidos.head())

print(unidos["demanda_mwh"].corr(unidos["temperatura_c"]))