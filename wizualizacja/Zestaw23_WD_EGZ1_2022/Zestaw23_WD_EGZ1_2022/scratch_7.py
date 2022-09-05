import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import ExcelFile
from pandas import ExcelWriter

#1
data1=[19.7, 18.8, 7.5, 22.1, 15.5, 16.4]
data2=[19.8, 17.2, 5.6, 21.1, 15.9, 20.3]
mylabels=["A","B","C","D","E","F"]
mycolors=["green", "tab:blue", "lightblue", "sandybrown", "tab:olive", "grey"]
myexplode=[0, 0.1, 0, 0, 0.1, 0]
plt.subplot(1,2,1)
plt.title("Lewo")
plt.pie(data1, colors=mycolors, labels=mylabels, explode=myexplode, startangle=30, autopct="%1.1f%%")
plt.subplot(1,2,2)
plt.title("Prawo")
plt.pie(data2, colors=mycolors, labels=mylabels, explode=myexplode, startangle=70, autopct="%1.1f%%")
plt.savefig("zad1.jpg")
plt.show()
#2
df1=pd.read_excel("ceny23.xlsx")
d11=df1.loc[df1["Rodzaje towarów"] == "cukier biały kryształ - za 1kg"]
d12=df1.loc[df1["Rodzaje towarów"] == "dżem - za 360g"]
x11=d11["Rok"]
x12=d12["Rok"]
y11=d11["Wartosc"]
y12=d12["Wartosc"]
plt.scatter(x11, y11, color="navy", marker="1", label="cukier biały kryształ - za 1kg")
plt.scatter(x12, y12, color="green", marker="*", label="dżem - za 360g")
plt.annotate(xy=(2015.5, 5.3), text="Szymon")
plt.grid()
plt.title("ceny23")
plt.xlabel("Rok")
plt.ylabel("Wartosc")
plt.savefig("zad2.png")
plt.show()
#3
df2=pd.read_csv("wynagrodzenia23.csv", sep=";")
datay=df2.iloc[:, 5:11]
datay=datay.replace('[^\d.]', '', regex=True).astype(float)
y21=datay.iloc[1:2,:]#kujawsko-pomorskie
y22=datay.iloc[3:4,:]#lubuskie
width=0.3

bar1=y21["2014"]
bar2=y21["2015"]
bar3=y21["2016"]
bar4=y21["2017"]
bar5=y21["2018"]
bar6=y21["2019"]
bar7=y22["2014"]
bar8=y22["2015"]
bar9=y22["2016"]
bar10=y22["2017"]
bar11=y22["2018"]
bar12=y22["2019"]

plt.bar(2014 - width/2, bar1, width, label='kujawsko-pomorskie', color="navy")
plt.bar(2014 + width/2, bar7, width, label='lubuskie', color="orange")
plt.bar(2015 - width/2, bar2, width, color="navy")
plt.bar(2015 + width/2, bar8, width, color="orange")
plt.bar(2016 - width/2, bar3, width, color="navy")
plt.bar(2016 + width/2, bar9, width, color="orange")
plt.bar(2017 - width/2, bar4, width, color="navy")
plt.bar(2017 + width/2, bar10, width, color="orange")
plt.bar(2018 - width/2, bar5, width, color="navy")
plt.bar(2018 + width/2, bar11, width, color="orange")
plt.bar(2019 - width/2, bar6, width, color="navy")
plt.bar(2019 + width/2, bar12, width, color="orange")
plt.title("zad3")
plt.xlabel("Rok")
plt.ylabel("Wartosc")
plt.legend(loc=3)
plt.grid()
plt.savefig("zad3.pdf")
plt.show()
