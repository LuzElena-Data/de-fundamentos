def clasificar(litros, umbral=1500):
    if litros > umbral:
        return "ALTO"
    else:
        return "normal"

print(clasificar(1610))
print(clasificar(1390))
print(clasificar(1390, 1000))




def total_medidor(lecturas, idvbox):
    T_litros=0
    for fila in lecturas:
        if fila['idvbox'] == idvbox:
            T_litros = T_litros+ fila['litros']
    return T_litros


lecturas = [
    {"idvbox": 7357, "fecha": "2026-10-20", "litros": 1480},
    {"idvbox": 7357, "fecha": "2026-10-21", "litros": 1525},
    {"idvbox": 5570, "fecha": "2026-10-20", "litros": 820},
]

print(total_medidor(lecturas, 7357))   # debe dar 3005
print(total_medidor(lecturas, 5570))   # debe dar 820


