import matplotlib.pyplot as plt
import pandas as pd

dane = pd.read_excel ("rod6.xlsx", header=None).T
dane2 = dane.iloc[1:, :]
dane2.columns = dane.iloc[0,:]
dane2["Rok"] = pd.Series(dane2["Rok"],dtype=int)
dane2["Wartosc"] = pd.Series(dane2["Wartosc"], dtype=int)
dzialki = dane2[dane2[ "Rodzaje terenu"] == "działki"]
dp = dzialki[dzialki["Ogrody"] == "powierzchnia"]

plt.barh(dp["Rok"], dp["Wartosc"])
plt.yticks(dp["Rok"])
plt.title("Dane o powierzchni działek")
plt.savefig("zad3.pdf")
plt.show()