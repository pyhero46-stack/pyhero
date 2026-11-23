"""Misión final: tus gastos de la semana con Pandas.

1. Lee gastos.xlsx (columnas: día, monto) y muestra el total.
2. BONUS: filtra los gastos mayores a 200 y guárdalos en un Excel nuevo.

Abre la terminal en esta carpeta y corre:  python mision.py
(Cambia gastos.xlsx por tu propio archivo con tus gastos).
"""
import pandas as pd

gastos = pd.read_excel("gastos.xlsx")
print(gastos["monto"].sum())

# --- BONUS ---
gastos_altos = gastos[gastos["monto"] > 200]
gastos_altos.to_excel("gastos_altos.xlsx", index=False)
print("Gastos mayores a 200 guardados en gastos_altos.xlsx")
