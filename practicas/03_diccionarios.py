#lectura = {"idvbox": 7357, "fecha": "2026-10-20", "litros": 1480}

#print(lectura)
#print(lectura["litros"])
#print(lectura["fecha"])

#print(lectura["consumo"])

#print(lectura.get("consumo"))
#print(lectura.get("consumo", 0))

#lectura["litros"] = 1500
#lectura["unidad"] = "L"
#print(lectura)


lecturas = [
    {"idvbox": 7357, "fecha": "2026-10-20", "litros": 1480},
    {"idvbox": 7357, "fecha": "2026-10-21", "litros": 1525},
    {"idvbox": 5570, "fecha": "2026-10-20", "litros": 820},
]



#for fila in lecturas:
#    print(f"Medidor {fila['idvbox']}: {fila['litros']} litros")

T_litros=0

for fila in lecturas:
        if fila['idvbox'] == 7357:
            T_litros = T_litros+ fila['litros']
print(f"Total Litros: {T_litros}")


