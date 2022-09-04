import matplotlib.pyplot as plt
import numpy as np

x = np.arange(6)
y = np.array([27, 38, 40, 26, 2, 8])
plt.barh(x, y, color="tab:pink", label="A")
y2 = np.array([-50, -27, -30, -44, -38, -42])
plt.barh(x, y2, color="tab:cyan", label="B")
plt.title("Wykres zmian A i B")
plt.legend()
m = ["Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec"]
plt.yticks(x, m, rotation=45)
plt.savefig("zad1.png")
plt.show()
