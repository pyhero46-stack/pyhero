# Misión del Episodio 1: grafica la temperatura de tu semana.
# Cambia los números por las temperaturas de tu ciudad.
import matplotlib.pyplot as plt

dias = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]
temperatura = [22, 24, 21, 25, 27, 26, 23]

plt.plot(dias, temperatura, marker="o", color="orange")  # BONUS: marker y color
plt.title("Temperatura de mi semana")
plt.xlabel("Día")
plt.ylabel("Temperatura (°C)")
plt.show()
