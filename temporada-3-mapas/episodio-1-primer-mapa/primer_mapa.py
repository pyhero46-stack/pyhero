import folium

mapa = folium.Map(location=[19.4326, -99.1332], zoom_start=12)
mapa.save("mapa.html")
