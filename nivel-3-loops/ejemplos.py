"""PyHero — Nivel 3: Los Loops

Todo el código que aparece en el video, en orden.
Córrelo con:  python ejemplos.py
"""

# --- Escena 2 — El ciclo for --------------------
jugadores = ["Ana", "Luis", "Mario", "Sara", "Pedro"]

for jugador in jugadores:
    print("Hola", jugador)

# --- Escena 2 — El ciclo for --------------------
for i in range(5):
    print("Vuelta", i)

# --- Escena 3 — El ciclo while --------------------
vida = 3

while vida > 0:
    print("Vidas restantes:", vida)
    vida -= 1

print("Game Over")

# --- Escena 4 — Boss: Generador de tablas --------------------
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")
