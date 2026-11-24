# Misión del Episodio 2: tus 3 lugares favoritos, cada uno con su popup.
# Aquí van 3 de Monterrey de ejemplo: cámbialos por los tuyos.
import folium

favoritos = [
    ["Macroplaza", 25.6694, -100.3098, "red"],
    ["Parque Fundidora", 25.6785, -100.2836, "green"],
    ["Cerro de la Silla", 25.6327, -100.2302, "purple"],
]

mapa = folium.Map(location=[25.6580, -100.2700], zoom_start=12)

for nombre, lat, lon, color in favoritos:
    folium.Marker([lat, lon], popup=nombre, tooltip=nombre,
                  icon=folium.Icon(color=color)).add_to(mapa)  # BONUS: cada uno de su color

mapa.save("mis_lugares.html")
