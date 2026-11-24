# Misión resuelta: el mismo código del Boss, pero con mis_sucursales.xlsx,
# que trae una fila nueva al final (Tienda PyHero Oaxaca). El Python no cambia: solo el Excel.

import folium
import pandas as pd


def color_por_ventas(ventas):
    if ventas >= 500000:
        return "green"
    elif ventas >= 250000:
        return "orange"
    else:
        return "red"


df = pd.read_excel("mis_sucursales.xlsx")
mapa = folium.Map(location=[23.5, -102.0], zoom_start=5)

for _, fila in df.iterrows():
    folium.Marker(
        [fila["lat"], fila["lon"]],
        popup=f"{fila['nombre']}: {fila['ventas']} pesos",
        tooltip=fila["ciudad"],
        icon=folium.Icon(color=color_por_ventas(fila["ventas"])),
    ).add_to(mapa)

mapa.save("mis_sucursales.html")
