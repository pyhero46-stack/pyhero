"""PyHero — Nivel 5: Pandas y Excel

Todo el código que aparece en el video, en orden.
Córrelo con:  python ejemplos.py
"""

# --- Escena 2 — ¿Qué es Pandas? --------------------
import pandas as pd

df = pd.read_excel("ventas.xlsx")
print(df.head())
print(df.describe())

# --- Escena 3 — Filtrar y analizar --------------------
# Filtrar ventas mayores a 1000
ventas_altas = df[df["monto"] > 1000]

# Agrupar por vendedor
resumen = df.groupby("vendedor")["monto"].sum()
print(resumen)

# --- Escena 4 — Boss Final: Reporte automático --------------------
import pandas as pd

# Leer datos
df = pd.read_excel("ventas.xlsx")

# Analizar
resumen = df.groupby("vendedor")["monto"].sum().reset_index()
resumen.columns = ["Vendedor", "Total Vendido"]

# Guardar reporte
resumen.to_excel("reporte_final.xlsx", index=False)
print("¡Reporte generado!")
