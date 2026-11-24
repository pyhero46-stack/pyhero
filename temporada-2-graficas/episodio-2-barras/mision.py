# Misión del Episodio 2: grafica tus gastos de la semana.
# Cambia gastos.xlsx por tu propio archivo (columnas: día, monto).
import pandas as pd
import matplotlib.pyplot as plt

gastos = pd.read_excel("gastos.xlsx")
gastos = gastos.sort_values("monto", ascending=False)  # BONUS: de mayor a menor

plt.bar(gastos["día"], gastos["monto"], color="teal")
plt.title("Mis gastos de la semana")
plt.ylabel("Pesos")
plt.tight_layout()
plt.savefig("gastos.png")
plt.show()
