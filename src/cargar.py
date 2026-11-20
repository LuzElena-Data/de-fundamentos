import os
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import URL, create_engine
from sqlalchemy import URL, create_engine, text

RAIZ = Path(__file__).parent.parent
load_dotenv(RAIZ / ".env")

url_bd = URL.create(
    "postgresql+psycopg2",
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_SERVER"),
    port=5432,
    database=os.getenv("DB_NAME"),
)
engine = create_engine(url_bd)

df = pd.read_csv(RAIZ / "data" / "demanda_clima.csv", parse_dates=["fecha"])
df["fecha"] = df["fecha"].dt.tz_localize("UTC")

df.to_sql("demanda_clima_stage", engine, if_exists="replace", index=False)

consulta = text("""
    INSERT INTO demanda_clima (fecha, demanda_mwh, temperatura_c)
    SELECT fecha, demanda_mwh, temperatura_c
    FROM demanda_clima_stage
    ON CONFLICT (fecha) DO NOTHING
""")

with engine.begin() as conexion:
    resultado = conexion.execute(consulta)
    print(f"Filas nuevas insertadas: {resultado.rowcount}")