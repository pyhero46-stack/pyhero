# Misión del Episodio 4: agrega una tercera gráfica al reporte.
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("ventas.xlsx")
vendedores = df.groupby("vendedor")["monto"].sum()
productos = df.groupby("producto")["monto"].sum().sort_values(ascending=False)
ranking = df.groupby("producto")["monto"].sum().sort_values()

fig, ejes = plt.subplots(1, 3, figsize=(18, 5))  # 1 fila, 3 columnas
ejes[0].bar(vendedores.index, vendedores.values, color=["blue", "orange", "green"])
ejes[0].set_title("Ventas por vendedor")
ejes[1].pie(productos.values, labels=productos.index, autopct="%1.0f%%", startangle=90)
ejes[1].set_title("Ventas por producto")
ejes[2].barh(ranking.index, ranking.values, color="purple")  # la tercera gráfica
ejes[2].set_title("Ranking de productos")
ejes[2].set_xlabel("Ventas en pesos")  # BONUS: con ejes, xlabel se vuelve set_xlabel
fig.suptitle("Reporte de ventas")
plt.tight_layout()
plt.savefig("reporte_completo.png")
plt.show()
