import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import ExcelFile
from pandas import ExcelWriter

# 1
fig, ax1 = plt.subplots()
plt.grid()
x = np.arange(-4, 4, 0.1)
y1 = pow(x, 2) - 1
y2 = -1*pow(x, 2) + 1
plt.title("Wykresy dwóch funkcji liniowych - wzory Latex")
ax1.plot(x, y1, color='tab:orange', label="y=x^2 - 1", linestyle='dashed')
plt.xticks(np.arange(-4, 4, 2))
plt.xlabel("oś pozioma", color="tab:pink")
plt.yticks(np.arange(0, 110, 20))
plt.ylabel("oś pionowa po lewej stronie", color="tab:purple")
plt.legend(loc=1)

ax2 = ax1.twinx()
ax2.plot(x, y2, color='tab:olive', label="y=-x^2 + 1", linestyle='dashdot')
plt.ylabel("oś pionowa po prawej stronie", color="tab:orange")
plt.yticks(np.arange(0, -110, -20))
plt.legend(loc=3)

plt.savefig("zad1.jpg")

plt.show()

# 2
df = pd.read_excel("handel34.xlsx")
df1 = df.loc[df["Wyszczególnienie"] == "stacje paliw"]
x2 = df1["Rok"]
y2 = df1["Wartosc"]
plt.bar(x2, y2, color='darkred', width=0.402, label="Wartość")
plt.xticks(np.arange(min(x2), max(x2)+1, 1))
plt.annotate(xy=(2011,100), text="Szymon", color="lime")
plt.xlabel("Rok")
plt.ylabel("Wartość")
plt.title("Stacje paliw - ilość w latach 2011-2020")
plt.grid()
plt.legend(loc=4)

plt.savefig("zad2.pdf")

plt.show()

# 3
df2 = pd.read_csv("wynagrodzenia34.csv", sep=';')
x31 = df2.loc[df2['Województwo'] == 'ŚWIĘTOKRZYSKIE']
x32 = df2.loc[df2['Województwo'] == 'MAŁOPOLSKIE']
x33 = df2.loc[df2['Województwo'] == 'PODKARPACKIE']
x31 = x31.iloc[:1, 1:]
x32 = x32.iloc[:1, 1:]
x33 = x33.iloc[:1, 1:]
x31t = np.transpose(x31)
x32t = np.transpose(x32)
x33t = np.transpose(x33)
print(x31t, x32t, x33t)

x31t=x31t.replace('[^\d.]', '', regex=True).astype(float)
print(x31t.dtypes)

x32t=x32t.replace('[^\d.]', '', regex=True).astype(float)
print(x32t.dtypes)

x33t=x33t.replace('[^\d.]', '', regex=True).astype(float)
print(x33t.dtypes)

plt.plot(x31t, color='navy', linestyle='dashdot', marker='*', label='ŚWIĘTOKRZYSKIE')
plt.plot(x32t, color='red', linestyle='dashed', marker='.', label='MAŁOPOLSKIE')
plt.plot(x33t, color='black', linestyle='dotted', marker='1', label='PODKARPACKIE')
plt.legend()
plt.grid()
plt.title('Wynagrodzenia w latach 2010-2019')
plt.xlabel('Rok')
plt.ylabel('Wynagrodzenie')
yt = ['300 tys', '350 tys', '400 tys', '450 tys', '500 tys']
plt.yticks([300000, 350000, 400000, 450000, 500000], yt, rotation=36)

plt.savefig("zad3.png")

plt.show()
