import matplotlib.pyplot as plt

meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun"]
ventas = [8200, 9500, 7800, 11200, 12600, 14300]

plt.plot(meses, ventas, marker="o", color="green")
plt.title("Ventas de la tienda")
plt.xlabel("Mes")
plt.ylabel("Ventas en pesos")
plt.grid(True)
plt.show()
