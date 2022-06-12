from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

wys = [10,15,18,22,27]
x = np.arange(0, len(wys))
k = ["black", "red", "green", "yellow", "pink"] # definiowanie wielu kolorow
plt.bar(x, wys, color = k, width=0.75) # dodanie wielu kolorow
etyk = ["Kategoria A", "Kategoria B", "Kategoria C", "Kategoria D", "Kategoria E"]
plt.xticks(x, etyk, rotation=45)
y2 = [20,30,40,50,60]
plt.plot(x,y2)
plt.title("tytul")
plt.tight_layout()
plt.show()
