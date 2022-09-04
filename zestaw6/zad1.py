import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.arange(6)
y1= np.array([35,38,20,26,37,35])
y2 =np.array([-15,-11,-14,-21, -18,-28])
m=["Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec"]
plt.bar(x,y1, color="forestgreen", label="X")
plt.bar(x,y2, color="red", label="Y")
plt.title("Wykres zmian X i Y")
plt.legend()
plt.xticks(x, m, rotation=35)
plt.tight_layout()
plt.savefig("zad1.png")
plt.show()