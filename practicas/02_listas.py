litros = [1480, 1525, 1610, 1390, 1575]

#print(litros)
#print(len(litros))
#print(litros[0])
#print(litros[-1])

litros.append(1600)
#print(litros)
#print(len(litros))

#print(litros)
#print(f"Total: {sum(litros)}")
#print(f"Maximo: {max(litros)}")
#print(f"Minimo: {min(litros)}")
#print(f"Cantidad: {len(litros)}")

#for valor in litros:
 #   print(valor)


#for valor in litros:
 #   if valor > 1500:
 #       print(f"{valor} -> ALTO")
 #   else:
 #       print(f"{valor} -> normal")

 #       altos = 0

#for valor in litros:
#    if valor > 1500:
#        altos = altos + 1

#print(f"Lecturas altas: {altos}")  

altos = 0

for valor in litros:
    if valor > 1500:
        altos = altos + valor

print(f"Litros en lecturas altas: {altos}")