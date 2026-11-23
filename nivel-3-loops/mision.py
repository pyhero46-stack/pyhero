"""Misión del Nivel 3: tus 3 videojuegos favoritos con un for.

BONUS: cuenta regresiva del 10 al 1 con un while, y al final ¡Despegue!
Córrelo con:  python mision.py
"""
juegos = ["PyHero", "Space Bits", "Pixel Kart"]

for juego in juegos:
    print("Me encanta", juego)

# --- BONUS ---
cuenta = 10
while cuenta > 0:
    print(cuenta)
    cuenta -= 1

print("¡Despegue!")
