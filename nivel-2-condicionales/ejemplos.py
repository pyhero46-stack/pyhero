"""PyHero — Nivel 2: Los Condicionales

Todo el código que aparece en el video, en orden.
Córrelo con:  python ejemplos.py
"""

# --- Escena 2 — ¿Qué es un if? --------------------
vida = 100

if vida > 0:
    print("¡PyHero sigue vivo!")
else:
    print("Game Over...")

# --- Escena 3 — elif: más de dos caminos --------------------
puntos = 85

if puntos >= 90:
    print("Rango S")
elif puntos >= 70:
    print("Rango A")
else:
    print("Sigue intentando")

# --- Escena 4 — Boss: Juego de adivinanza --------------------
secreto = 42
intento = 50

if intento > secreto:
    print("Muy alto")
elif intento < secreto:
    print("Muy bajo")
else:
    print("¡Adivinaste!")
