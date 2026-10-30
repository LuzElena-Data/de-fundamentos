"""Carga la configuracion del proyecto desde el archivo .env."""
import os
from pathlib import Path

from dotenv import load_dotenv

RAIZ = Path(__file__).resolve().parent.parent
load_dotenv(RAIZ / ".env")

VARIABLES = ("DB_SERVER", "DB_NAME", "DB_USER", "DB_PASSWORD")


def validar() -> None:
    """Falla con un mensaje claro si falta alguna variable."""
    faltantes = [nombre for nombre in VARIABLES if not os.getenv(nombre)]
    if faltantes:
        raise RuntimeError(f"Faltan variables en .env: {', '.join(faltantes)}")


if __name__ == "__main__":
    validar()
    print(f"Servidor: {os.getenv('DB_SERVER')}")
    print(f"Base:     {os.getenv('DB_NAME')}")
    print(f"Usuario:  {os.getenv('DB_USER')}")
    print(f"Password: {'*' * len(os.getenv('DB_PASSWORD'))}")