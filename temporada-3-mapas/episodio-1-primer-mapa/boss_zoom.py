import folium

for zoom in [2, 6, 10, 16]:
    mapa = folium.Map(location=[19.4326, -99.1332], zoom_start=zoom)
    mapa.save(f"zoom_{zoom}.html")
