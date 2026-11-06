lecturas_texto = ["1480", "1525", "N/A", "1390"]
rechazados=[]

# total = 0
# for valor in lecturas_texto:
#     total = total + int(valor)

# print(f"Total: {total}")


lecturas_texto.append("")
cantidad=0
conteo=0
total = 0

for valor in lecturas_texto:
    conteo=conteo+1
    try:
        total = total + int(valor)
        
    except ValueError:
        print(f"Valor invalido, se omite: {valor}")
        cantidad=cantidad+1
        rechazados.append(valor)

print(f"Total: {total}")
print(f"Cantidad Rechazados: {cantidad}")
print(f"Lecturas validas: {len(lecturas_texto) - len(rechazados)}")
print(f"Cantidad Total: {conteo}")
print(f"Rechazados: {rechazados}")