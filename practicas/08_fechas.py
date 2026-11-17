import pandas as pd

hora_eia = "2026-11-01T00"
hora_clima = "2026-11-01T00:00"

print(hora_eia == hora_clima)

fecha_eia = pd.to_datetime(hora_eia, format="%Y-%m-%dT%H")
#fecha_clima = pd.to_datetime(hora_clima, format="%Y-%m-%dT%H")
fecha_clima = pd.to_datetime(hora_clima, format="%Y-%m-%dT%H:%M")

print(fecha_eia)
print(fecha_clima)
print(fecha_eia == fecha_clima)