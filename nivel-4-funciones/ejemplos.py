"""PyHero — Nivel 4: Las Funciones

Todo el código que aparece en el video, en orden.
Córrelo con:  python ejemplos.py
"""

# --- Escena 2 — ¿Qué es una función? --------------------
def saludar(nombre):
    return f"Hola, {nombre}! Bienvenido a PyHero."

print(saludar("Ana"))
print(saludar("Luis"))

# --- Escena 3 — Parámetros y retorno --------------------
def calcular_daño(ataque, defensa):
    daño = ataque - defensa
    if daño < 0:
        daño = 0
    return daño

resultado = calcular_daño(50, 30)
print("Daño causado:", resultado)

# --- Escena 4 — Boss: Conversor de unidades --------------------
def km_a_millas(km):
    return round(km * 0.621371, 2)

print(km_a_millas(10))
print(km_a_millas(100))
