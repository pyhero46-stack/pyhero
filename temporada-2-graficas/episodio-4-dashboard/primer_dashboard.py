import matplotlib.pyplot as plt

dias = ["Lun", "Mar", "Mié", "Jue", "Vie"]
xp = [10, 25, 20, 40, 55]
monedas = [3, 8, 5, 12, 9]

fig, ejes = plt.subplots(1, 2)
ejes[0].plot(dias, xp)
ejes[0].set_title("Mi XP")
ejes[1].bar(dias, monedas)
ejes[1].set_title("Mis monedas")
plt.show()
