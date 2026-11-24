# 🎮 PyHero: aprende Python como un videojuego

Código de los videos del canal **PyHero**: un curso de Python desde cero, en español, con estética de videojuego retro. Cada nivel tiene su explicación, su Boss y una misión para ti.

Aquí está **todo el código que sale en los videos**, listo para copiar, correr y modificar, y las **misiones resueltas** (con bonus) para que compares tu solución.

> 📺 Playlist del curso: [link de la playlist]

## El curso

| Nivel | Tema | Carpeta | Qué hay |
| --- | --- | --- | --- |
| 1 | Variables | [`nivel-1-variables`](nivel-1-variables) | Variables, `type()`, mini calculadora |
| 2 | Condicionales | [`nivel-2-condicionales`](nivel-2-condicionales) | `if`, `elif`, `else`, juego de adivinanza |
| 3 | Loops | [`nivel-3-loops`](nivel-3-loops) | `for`, `range()`, `while`, tabla de multiplicar |
| 4 | Funciones | [`nivel-4-funciones`](nivel-4-funciones) | `def`, parámetros, `return`, conversor km → millas |
| 5 | Pandas y Excel | [`nivel-5-pandas-excel`](nivel-5-pandas-excel) | Leer, filtrar y agrupar un Excel, reporte automático |

En cada carpeta:

- `ejemplos.py`: el código del video, en el mismo orden.
- `mision.py`: la misión del nivel resuelta, con el bonus.
- (Nivel 5) `ventas.xlsx` y `gastos.xlsx`: los archivos de ejemplo.

## Temporada 2: Gráficas

| Episodio | Tema | Carpeta |
| --- | --- | --- |
| 1 | Tu primera gráfica: líneas | [`temporada-2-graficas/episodio-1-lineas`](temporada-2-graficas/episodio-1-lineas) |
| 2 | Gráficas de barras con datos de Excel | [`temporada-2-graficas/episodio-2-barras`](temporada-2-graficas/episodio-2-barras) |
| 3 | Gráficas de pastel: qué parte le toca a cada uno | [`temporada-2-graficas/episodio-3-pastel`](temporada-2-graficas/episodio-3-pastel) |

## Proyectos

Proyectos completos y funcionales que puedes adaptar a tu trabajo:

| Proyecto | Qué hace |
| --- | --- |
| [🗺️ Mapa de sucursales](proyectos/mapa-sucursales) | Mapa interactivo con marcadores por color, mapa de calor y leyenda (Pandas + Folium) |

## Cómo empezar

1. Instala **Python 3** desde [python.org](https://www.python.org/downloads/). En Windows, marca la casilla **"Add Python to PATH"**.
2. Descarga este repositorio: botón verde **Code → Download ZIP**, y descomprímelo.
3. Instala las librerías (solo hacen falta para el Nivel 5, la Temporada 2 y los proyectos):

   ```bash
   pip install -r requirements.txt
   ```

4. Abre una terminal **dentro de la carpeta** del nivel y corre el archivo:

   ```bash
   cd nivel-3-loops
   python ejemplos.py
   ```

> 💡 Si un loop no se detiene (loop infinito), presiona **Ctrl + C** en la terminal.

## Licencia

Código libre bajo la licencia MIT: úsalo, cámbialo y compártelo.
