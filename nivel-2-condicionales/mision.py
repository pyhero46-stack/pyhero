"""Misión del Nivel 2: ¿el jugador puede pasar?

- 18 o más  -> Puedes pasar
- BONUS: exactamente 17 -> ya casi
- menos     -> Acceso denegado

Cambia la edad y vuelve a correrlo:  python mision.py
"""
edad = 17

if edad >= 18:
    print("Puedes pasar")
elif edad == 17:
    print("¡Ya casi! El próximo año pasas")
else:
    print("Acceso denegado")
