import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dane = pd.read_excel("samochody10.xlsx", header=None).T
dane.columns = ["Pojazd", "Rok", "Wartość"]
dane ["Rok"] = pd.Series(dane["Rok"], dtype=int)
dane ["Wartość"] = pd.Series(dane ["Wartość"], dtype=int)
rok17 = dane[dane["Rok"]==2017]
rok18 = dane[dane["Rok"]==2018]
x=np.arange(6)
plt.bar(x-0.165, rok17 ["Wartość"], width=0.33, label="2017")
plt.bar(x+0.165, rok18 ["Wartość"], width=0.33, label="2018")
plt.legend()
plt.xticks(x, rok17["Pojazd"], rotation=45)
plt.yticks([0, 0.5e7, 1e7, 1.5e7, 2e7], [0, "5ml", "10mln", "15mln", "20mln"])
plt.grid()
plt.tight_layout()
plt.savefig("zad3.pdf")
plt.show()
