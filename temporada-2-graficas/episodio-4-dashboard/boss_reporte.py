import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("ventas.xlsx")
vendedores = df.groupby("vendedor")["monto"].sum()
productos = df.groupby("producto")["monto"].sum().sort_values(ascending=False)

fig, ejes = plt.subplots(1, 2, figsize=(12, 5))
ejes[0].bar(vendedores.index, vendedores.values, color=["blue", "orange", "green"])
ejes[0].set_title("Ventas por vendedor")
ejes[1].pie(productos.values, labels=productos.index, autopct="%1.0f%%", startangle=90)
ejes[1].set_title("Ventas por producto")
fig.suptitle("Reporte de ventas")
plt.tight_layout()
plt.savefig("reporte.png")
plt.show()
