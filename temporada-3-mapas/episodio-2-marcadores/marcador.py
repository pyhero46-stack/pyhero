import folium

mapa = folium.Map(location=[19.4326, -99.1332], zoom_start=16)

folium.Marker(
    [19.4326, -99.1332],
    popup="¡Aquí es el Zócalo!",
    tooltip="Dame clic",
    icon=folium.Icon(color="red"),
).add_to(mapa)

mapa.save("marcador.html")
