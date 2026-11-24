import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("ventas.xlsx")
ranking = df.groupby("producto")["monto"].sum().sort_values()

plt.barh(ranking.index, ranking.values, color="purple")
plt.title("Ranking de productos")
plt.xlabel("Ventas en pesos")
plt.tight_layout()
plt.savefig("ranking.png")
plt.show()
