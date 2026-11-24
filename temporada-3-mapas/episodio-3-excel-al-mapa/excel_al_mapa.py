import folium
import pandas as pd

df = pd.read_excel("sucursales.xlsx")

mapa = folium.Map(location=[23.5, -102.0], zoom_start=5)

for _, fila in df.iterrows():
    folium.Marker(
        [fila["lat"], fila["lon"]],
        popup=fila["nombre"],
        tooltip=fila["ciudad"],
    ).add_to(mapa)

mapa.save("sucursales.html")
