import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("ventas.xlsx")
resumen = df.groupby("vendedor")["monto"].sum()

plt.bar(resumen.index, resumen.values, color=["blue", "orange", "green"])
plt.title("Ventas por vendedor")
plt.ylabel("Ventas en pesos")
plt.savefig("ventas.png")
plt.show()
