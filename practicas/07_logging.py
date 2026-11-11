import logging
from pathlib import Path

RUTA_LOG = Path(__file__).parent / "clima.log"


logging.basicConfig(
    level=logging.INFO,
    #level=logging.WARNING,
    format="%(asctime)s - %(levelname)s - %(message)s",
     filename=RUTA_LOG,
)

print("Esto es un print")
logging.info("Iniciando consulta a la API")
logging.warning("La humedad esta muy baja")
logging.error("La API no respondio")