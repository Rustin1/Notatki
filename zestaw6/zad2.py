import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dane = pd.read_excel("uczniowie6.xlsx")
rok = dane["Rok"]
wart = dane["Wartość"]
plt.plot(rok, wart, color="brown", linewidth=3)
plt.annotate(xy=[2015, 600000], text="13:14")
plt.xticks(rok, rok)
plt.xlabel("Rok")
plt.ylabel("Wartości")
plt.title("Dane o uczniach w Polsce w latach 2015-2019")
plt.tight_layout()
plt.savefig("zad2.jpg")
plt.show()