# Misión del Episodio 1: el mapa de tu ciudad.
# Busca tu ciudad en Google Maps, dale clic derecho y copia las coordenadas.
# Aquí va Monterrey de ejemplo: cámbialas por las tuyas.
import folium

mapa = folium.Map(location=[25.6866, -100.3161], zoom_start=13,
                  tiles="Esri.WorldImagery")  # BONUS: vista de satélite
mapa.save("mi_ciudad.html")
