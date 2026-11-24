# Misión del Episodio 3: el pastel de tu presupuesto del mes.
# Cambia los gastos y los montos por los tuyos.
import matplotlib.pyplot as plt

gastos = ["Renta", "Comida", "Transporte", "Diversión", "Ahorro"]
montos = [4000, 3000, 1200, 800, 1000]

separar = [0, 0, 0, 0, 0.1]  # BONUS: separa la rebanada del ahorro
plt.pie(montos, labels=gastos, autopct="%1.0f%%", explode=separar, startangle=90)
plt.title("Mi presupuesto del mes")
plt.savefig("presupuesto.png")
plt.show()
