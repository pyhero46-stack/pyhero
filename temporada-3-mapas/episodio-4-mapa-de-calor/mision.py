# Misión resuelta: el mismo mapa del Boss, pero el calor mide los clientes.
# Solo cambian el peso, el nombre de la capa y el archivo.

import folium
import pandas as pd
from folium.plugins import HeatMap


def color_por_ventas(ventas):
    if ventas >= 500000:
        return "green"
    elif ventas >= 250000:
        return "orange"
    else:
        return "red"


df = pd.read_excel("sucursales.xlsx")
mapa = folium.Map(location=[23.5, -102.0], zoom_start=5)

# capa 1: las tiendas, con su color
tiendas = folium.FeatureGroup(name="Tiendas")
for _, fila in df.iterrows():
    folium.Marker(
        [fila["lat"], fila["lon"]],
        popup=f"{fila['nombre']}: {fila['ventas']} pesos",
        icon=folium.Icon(color=color_por_ventas(fila["ventas"])),
    ).add_to(tiendas)
tiendas.add_to(mapa)

# capa 2: el calor de los CLIENTES (antes eran las ventas)
df["peso"] = df["clientes"] / df["clientes"].max()
puntos = df[["lat", "lon", "peso"]].values.tolist()
HeatMap(puntos, name="Calor de clientes", radius=35, blur=15, max_zoom=5).add_to(mapa)

folium.LayerControl().add_to(mapa)
mapa.fit_bounds(df[["lat", "lon"]].values.tolist())

mapa.save("mapa_clientes.html")
