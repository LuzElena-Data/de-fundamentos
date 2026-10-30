"""Estadisticas basicas de lecturas de medidores."""
from pathlib import Path

import pandas as pd

RUTA_DATOS = Path(__file__).resolve().parent.parent / "data" / "lecturas.csv"


def cargar_lecturas(ruta: Path) -> pd.DataFrame:
    """Lee el CSV de lecturas y convierte la fecha a tipo fecha."""
    return pd.read_csv(ruta, parse_dates=["fecha"])


def resumen_por_medidor(df: pd.DataFrame) -> pd.DataFrame:
    """Total, promedio, minimo y maximo de litros por medidor."""
    return (
        df.groupby("idvbox")["litros"]
        .agg(total="sum", promedio="mean", minimo="min", maximo="max", dias="count")
        .round(1)
    )


def dia_mayor_consumo(df: pd.DataFrame) -> pd.DataFrame:
    """Fila con el mayor consumo de cada medidor."""
    idx = df.groupby("idvbox")["litros"].idxmax()
    return df.loc[idx, ["idvbox", "fecha", "litros"]]


def main() -> None:
    df = cargar_lecturas(RUTA_DATOS)
    print(f"Lecturas cargadas: {len(df)} filas, {df['idvbox'].nunique()} medidores\n")
    print("Resumen por medidor:")
    print(resumen_por_medidor(df), "\n")
    print("Dia de mayor consumo por medidor:")
    print(dia_mayor_consumo(df).to_string(index=False))


if __name__ == "__main__":
    main()