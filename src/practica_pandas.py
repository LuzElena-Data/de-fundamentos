import pandas as pd

df = pd.read_csv("data/lecturas.csv")

# print(df)
# print(df.shape)
# print(df.columns)
# print(df.head(3))

#print(f"Total: {df['litros'].sum()}")
#print(f"Promedio: {df['litros'].mean()}")
#print(f"Maximo: {df['litros'].max()}")
#print(f"Minimo: {df['litros'].min()}")
#print(f"Cantidad: {df['litros'].count()}")





print(df[(df["idvbox"] == 7357)].sort_values("litros", ascending=False))