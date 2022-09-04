import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dane = pd.read_excel ("produkcja1.xlsx")
x = dane["Rok"]
y = dane["Wartość"]
plt.scatter(x,y, color= 'darkgreen', marker='^')
plt.title("Wykres wartości względem lat w Polsce")
plt.xlabel("Lata")
yt = [1280000, 1400080, 1600000]
ytz = ["1.2", "1.4", "1.6"]
plt.ylabel("w mln zł")
plt.yticks(yt,ytz)
plt.annotate(xy=[2018.5, 1150000], text="18:12")
plt.grid()
plt.savefig("zad2.pdf")
plt.show()