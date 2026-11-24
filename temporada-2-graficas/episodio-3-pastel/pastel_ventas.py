import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("ventas.xlsx")
resumen = df.groupby("vendedor")["monto"].sum()

plt.pie(resumen.values, labels=resumen.index, autopct="%1.0f%%")
plt.title("¿Quién vendió qué parte?")
plt.savefig("pastel.png")
plt.show()
