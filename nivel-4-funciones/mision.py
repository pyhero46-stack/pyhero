"""Misión del Nivel 4: una función que convierta Celsius a Fahrenheit.

Fórmula: c * 1.8 + 32
BONUS: una función que reciba dos números y devuelva el mayor.
Córrelo con:  python mision.py
"""


def celsius_a_fahrenheit(c):
    return c * 1.8 + 32


print(celsius_a_fahrenheit(30))   # 86.0


# --- BONUS ---
def mayor(a, b):
    if a > b:
        return a
    return b


print(mayor(7, 12))   # 12
