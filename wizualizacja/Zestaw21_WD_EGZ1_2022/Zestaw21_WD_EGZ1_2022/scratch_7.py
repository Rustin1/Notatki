import pandas as pd
from pandas import ExcelFile
from pandas import ExcelWriter
import numpy as np
import matplotlib.pyplot as plt

#1
dane1 = np.array([7.56, 15.7, 25.58, 16.86, 21.51, 12.79])
dane2 = np.array([16.67, 20.37, 17.59, 9.72, 19.91, 15.74])
mylabels = ["F", "A", "B", "C", "D", "E"]
myexplode = [0, 0, 0.1, 0, 0, 0]
mycolors = ["tab:blue", "tab:brown", "orchid", "tan", "lime", "tab:brown"]
plt.subplot(2, 2, 1)
plt.title("Lewo Góra")
plt.pie(dane1, labels=mylabels, explode=myexplode, autopct='%1.2f%%', colors=mycolors)
plt.subplot(2, 2, 4)
plt.title("Prawo Dół")
plt.pie(dane2, labels=mylabels, explode=myexplode, autopct='%1.2f%%', colors=mycolors)
plt.savefig("zad1.jpg")
plt.show()

#2
df1 = pd.read_excel("ceny21.xlsx")
df11 = df1.loc[df1["Rodzaje towarów"] == "mąka pszenna - za 1kg"]
df12 = df1.loc[df1["Rodzaje towarów"] == "kasza jęczmienna - za 0,5kg"]
x11 = df11["Rok"]
y11 = df11["Wartość"]
x12 = df12["Rok"]
y12 = df12["Wartość"]
plt.scatter(x11, y11, color="red", label="mąka")
plt.scatter(x12, y12, color="navy", label="kasza")
plt.legend(loc=3)
plt.grid()
plt.yticks(np.arange(2.0, 3.1, 0.1))
yt = [2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0]
ytz = ["2.00 zł", "2.10 zł", "2.20 zł", "2.30 zł", "2.40 zł", "2.50 zł", "2.60 zł", "2.70 zł", "2.80 zł", "2.90 zł", "3.00 zł"]
plt.yticks(yt, ytz, rotation=27)
plt.xlabel("Rok")
plt.ylabel("Cena")
plt.title("Wykres punktowy cen")
plt.savefig("zad2.png")
plt.show()

#3
df2 = pd.read_csv("wynagrodzenia21.csv", sep=";")
x21 = df2.loc[df2["Województwo"] == "OPOLSKIE"]
x22 = df2.loc[df2["Województwo"] == "POMORSKIE"]
x21 = x21.iloc[0:,1:]
x22 = x22.iloc[0:,1:]
x21 = x21.replace('[^\d.]', '', regex=True).astype(float)
x22 = x22.replace('[^\d.]', '', regex=True).astype(float)
x21 = np.transpose(x21)
x22 = np.transpose(x22)
x21 = x21.iloc[:4]
x22 = x22.iloc[:4]
x21 = np.transpose(x21)
x22 = np.transpose(x22)

bar1 = x22["2010"]
bar2 = x22["2011"]
bar3 = x22["2012"]
bar4 = x22["2013"]

bar5 = x21["2010"]
bar6 = x21["2011"]
bar7 = x21["2012"]
bar8 = x21["2013"]

bwidth = 0.47

plt.barh(2010 - bwidth/2, bar1, color='navy', height=bwidth, label="POMORSKIE")
plt.barh(2011 - bwidth/2, bar2, color='navy', height=bwidth)
plt.barh(2012 - bwidth/2, bar3, color='navy', height=bwidth)
plt.barh(2013 - bwidth/2, bar4, color='navy', height=bwidth)

plt.barh(2010 + bwidth/2, bar5, color='green', height=bwidth, label="OPOLSKIE")
plt.barh(2011 + bwidth/2, bar6, color='green', height=bwidth)
plt.barh(2012 + bwidth/2, bar7, color='green', height=bwidth)
plt.barh(2013 + bwidth/2, bar8, color='green', height=bwidth)

plt.title("Wykres województw - Opolskie, Pomorskie")
plt.yticks(np.arange(2010, 2014, 1))
plt.xticks([50000, 100000, 150000, 200000, 250000, 300000, 350000, 400000], ["50 tys", "100 tys",
                                                                             "150 tys", "200 tys", "250 tys", "300 tys",
                                                                             "350 tys", "400 tys"])
plt.legend()
plt.grid()
plt.savefig("zad3.pdf")
plt.show()
