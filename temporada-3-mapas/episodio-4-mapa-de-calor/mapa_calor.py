import folium
import pandas as pd
from folium.plugins import HeatMap

df = pd.read_excel("sucursales.xlsx")
mapa = folium.Map(location=[23.5, -102.0], zoom_start=5)

df["peso"] = df["ventas"] / df["ventas"].max()
puntos = df[["lat", "lon", "peso"]].values.tolist()

HeatMap(puntos, radius=35, blur=15, max_zoom=5).add_to(mapa)

mapa.save("mapa_calor.html")
