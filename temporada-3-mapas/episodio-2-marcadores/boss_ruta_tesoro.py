import folium

pistas = [
    ["Zócalo", 19.4326, -99.1332],
    ["Bellas Artes", 19.4352, -99.1412],
    ["Ángel de la Independencia", 19.4270, -99.1677],
]

mapa = folium.Map(location=[19.4280, -99.1580], zoom_start=14)

for nombre, lat, lon in pistas:
    folium.Marker([lat, lon], popup=nombre, tooltip=nombre).add_to(mapa)

# el tesoro: un marcador distinto a los demás
folium.Marker([19.4204, -99.1819], popup="¡El tesoro!",
              icon=folium.Icon(color="orange", icon="star")).add_to(mapa)

mapa.save("ruta_tesoro.html")
