import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("ventas.xlsx")
productos = df.groupby("producto")["monto"].sum().sort_values(ascending=False)

separar = [0.1, 0, 0, 0, 0, 0]
plt.pie(productos.values, labels=productos.index, autopct="%1.0f%%",
        explode=separar, startangle=90)
plt.title("¿Qué parte vende cada producto?")
plt.savefig("productos.png")
plt.show()
