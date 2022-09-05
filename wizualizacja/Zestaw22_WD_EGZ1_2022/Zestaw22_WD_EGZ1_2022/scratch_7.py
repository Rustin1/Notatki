import pandas as pd
from pandas import ExcelFile
from pandas import ExcelWriter
import numpy as np
import matplotlib.pyplot as plt

#1
dane1=[15.7, 25.6, 16.9, 21.5, 12.8, 7.6]
dane2=[20.4, 17.6, 9.7, 19.9, 15.7, 16.7]
myexplode=[0, 0.1, 0, 0, 0, 0]
mylabels=["A", "B", "C", "D", "E", "F"]
mycolors=["tab:brown", "tab:pink", "tan", "lime", "tab:brown", "tab:blue"]
plt.subplot(2,2,2)
plt.pie(dane1, colors=mycolors, explode=myexplode, labels=mylabels, startangle=40, autopct="%1.1f%%")
plt.title("Prawo Góra")
plt.subplot(2,2,3)
plt.pie(dane2, colors=mycolors, explode=myexplode, labels=mylabels, startangle=45, autopct="%1.1f%%")
plt.title("Lewo Dół")
plt.savefig("zad1.jpg")
plt.show()

#2
df1=pd.read_excel("ceny22.xlsx")
df11=df1.loc[df1["Rodzaje towarów"]=="bułka pszenna - za 50g"]
df12=df1.loc[df1["Rodzaje towarów"]=="chleb pszenno-żytni - za 0,5kg"]
xb=df11["Rok"]
xc=df12["Rok"]
yb=df11["Wartość"]
yc=df12["Wartość"]
plt.scatter(xb, yb, color="green", marker="*", label="bułka")
plt.scatter(xc, yc, color="blue", marker="1", label="chleb")
plt.title("Ceny pieczywa w latach 2009-2014")
plt.legend()
plt.grid()
plt.xlabel("Rok")
plt.ylabel("Wartość w zł")
plt.savefig("zad2.png")
plt.show()

#3
df2=pd.read_csv("wynagrodzenia22.csv", sep=";")
df2copy=df2.iloc[:, 1:]
df2copy=df2copy.replace('[^\d.]', '', regex=True).astype(float) #nwm czy ta formuła na zamianę typu string na float jest poprawna(działa, ale nwm czy tak mogę robić)
df2v=df2copy.iloc[:, 3:8]
y11=df2v.iloc[4:5] # ŁÓDZKIE
y12=df2v.iloc[11:12] # ŚLĄSKIE
#y11=np.transpose(y11)
#y12=np.transpose(y12)

bwidth = 0.3
bar1=y11["2013"]
bar2=y12["2013"]
bar3=y11["2014"]
bar4=y12["2014"]
bar5=y11["2015"]
bar6=y12["2015"]
bar7=y11["2016"]
bar8=y12["2016"]
bar9=y11["2017"]
bar10=y12["2017"]

#plt.bar(2013 - bwidth/2, y11, bwidth, label='ŁÓDZKIE')# zawsze przyjmuje wartość 4(nwm dlaczego, ale wydaje mi się że za wartość pobiera indeks)
#plt.bar(2013 + bwidth/2, y12, bwidth, label='ŚLĄSKIE') zawsze przyjmuje wartość 11(nwm dlaczego, ale wydaje mi się że za wartość pobiera indeks)

#wykres zrobiony na piechotę(czy mogę tak robić \/)
plt.barh(2013 - bwidth/2, bar1, bwidth, color="k", label="ŁÓDZKIE")
plt.barh(2013 + bwidth/2, bar2, bwidth, color="red", label="ŚLĄSKIE")
plt.barh(2014 - bwidth/2, bar3, bwidth, color="k")
plt.barh(2014 + bwidth/2, bar4, bwidth, color="red")
plt.barh(2015 - bwidth/2, bar5, bwidth, color="k")
plt.barh(2015 + bwidth/2, bar6, bwidth, color="red")
plt.barh(2016 - bwidth/2, bar7, bwidth, color="k")
plt.barh(2016 + bwidth/2, bar8, bwidth, color="red")
plt.barh(2017 - bwidth/2, bar9, bwidth, color="k")
plt.barh(2017 + bwidth/2, bar10, bwidth, color="red")

plt.title("Wynagrodzenie w latach 2013-2017")
plt.ylabel("Rok")
plt.xlabel("Wynagrodzenie")
plt.xticks([0,100000,200000,300000,400000], ["0", "100 tys", "200 tys", "300 tys", "400 tys"])
plt.grid()
plt.legend()
plt.savefig("zad3.pdf")
plt.show()