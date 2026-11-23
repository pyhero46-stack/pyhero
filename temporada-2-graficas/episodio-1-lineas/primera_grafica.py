import matplotlib.pyplot as plt

dias = ["Lun", "Mar", "Mié", "Jue", "Vie"]
xp = [10, 25, 20, 40, 55]

plt.plot(dias, xp)
plt.title("Mi XP de la semana")
plt.xlabel("Día")
plt.ylabel("Puntos de XP")
plt.show()
