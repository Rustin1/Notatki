import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

#1

danex=[12,13.3,13.5,17.25]
daney=[15.8,17.1,13.75,19.5]
mycolors=["tab:orange", "grey", "grey", "tab:cyan"]
plt.scatter(danex, daney, linewidths=3.7, color=mycolors, marker="x")
plt.grid()
plt.xticks(color="tab:blue")
plt.yticks(color="tab:orange")
plt.title("Wykres punktowy - 4 krzyżyki")
plt.xlabel("Oś pozioma", color="tab:olive")
plt.ylabel("Oś pionowa", color="tab:pink")
plt.tight_layout()
plt.show()

#2

df1=pd.read_excel("handel24.xlsx")
df1=df1.loc[df1["Wyszczególnienie"] == "sklepy"]
x1=df1["Rok"]
y1=df1["Wartosc"]
plt.plot(x1, y1, color="tab:red", linestyle='dashed', linewidth=0.666, marker="*", label="sklepy")
plt.annotate(xy=(2019.5, 320000), text="Szymon", color="navy")
plt.grid()
plt.xlabel("Rok", rotation=10, color="blue")
plt.ylabel("Wartość", color="orange")
plt.title("zad2", color="grey")
plt.xticks(np.arange(2011, 2021, 1))
plt.yticks([320000,330000,340000,350000,360000], ["320 tys", "330 tys", "340 tys", "350 tys", "360 tys"])
plt.legend()
plt.show()

#3

df2=pd.read_csv("pogoda24.csv", sep=";")
t=df2["Temperatura"]
o=df2["Opad"]
w=df2["Wiatr"]
koszyk1=pd.cut(df2, w)
