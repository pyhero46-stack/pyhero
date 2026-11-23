"""Mapa interactivo de sucursales con Python (Pandas + Folium).

Lee las sucursales de sucursales.csv y crea mapa_sucursales.html con:
  - un marcador por sucursal (verde, naranja o rojo según sus ventas),
  - un mapa de calor que pesa más donde se vende más,
  - un selector de capas y una leyenda.

Córrelo con:  python mapa.py
Al terminar se abre el mapa en tu navegador.
"""
import webbrowser
from pathlib import Path

import folium
import pandas as pd
from folium.plugins import HeatMap

# Así encuentra los archivos aunque corras el script desde otra carpeta
CARPETA = Path(__file__).resolve().parent

# 1. Leer las sucursales
#    ¿Tus datos están en Excel? Usa:  pd.read_excel(CARPETA / "sucursales.xlsx")
df = pd.read_csv(CARPETA / "sucursales.csv")

# 2. Mapa base, centrado en el promedio de todas las coordenadas
centro = [df["lat"].mean(), df["lon"].mean()]
mapa = folium.Map(location=centro, zoom_start=5)


# 3. Un marcador por sucursal, con color según sus ventas
def color_por_ventas(ventas):
    if ventas >= 500_000:
        return "green"
    elif ventas >= 250_000:
        return "orange"
    else:
        return "red"


marcadores = folium.FeatureGroup(name="Sucursales")
for _, fila in df.iterrows():
    texto = f"<b>{fila['nombre']}</b><br>{fila['ciudad']}<br>Ventas: ${fila['ventas']:,}"
    folium.Marker(
        location=[fila["lat"], fila["lon"]],
        popup=folium.Popup(texto, max_width=250),   # se ve al dar clic
        tooltip=fila["nombre"],                     # se ve al pasar el mouse
        icon=folium.Icon(color=color_por_ventas(fila["ventas"]), icon="shopping-cart", prefix="fa"),
    ).add_to(marcadores)
marcadores.add_to(mapa)

# 4. Mapa de calor: cada punto pesa según sus ventas (de 0 a 1)
df["peso"] = df["ventas"] / df["ventas"].max()
calor = df[["lat", "lon", "peso"]].values.tolist()
HeatMap(calor, name="Mapa de calor (ventas)", radius=40, blur=25).add_to(mapa)

# 5. Zoom automático para que se vean todas las sucursales,
#    selector de capas (arriba a la derecha) y leyenda (abajo a la izquierda)
mapa.fit_bounds(df[["lat", "lon"]].values.tolist(), padding=(30, 30))
folium.LayerControl().add_to(mapa)
leyenda = """
<div style="position: fixed; bottom: 30px; left: 30px; z-index: 9999; background: white;
            padding: 10px 14px; border-radius: 8px; box-shadow: 0 0 6px rgba(0,0,0,.3);
            font-family: sans-serif; font-size: 14px;">
  <b>Ventas del mes</b><br>
  <span style="color: green;">&#9679;</span> $500,000 o más<br>
  <span style="color: orange;">&#9679;</span> $250,000 a $499,999<br>
  <span style="color: red;">&#9679;</span> menos de $250,000
</div>
"""
mapa.get_root().html.add_child(folium.Element(leyenda))

# 6. Guardar como página web y abrirla
salida = CARPETA / "mapa_sucursales.html"
mapa.save(salida)
print(f"¡Mapa listo! {salida}")
webbrowser.open(salida.as_uri())
