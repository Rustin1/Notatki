import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import ExcelWriter
from pandas import ExcelFile

# zad1
C = (61, 54, 44, 58, 53)
B = (43, 42, 29, 39, 40)
A = (27, 33, 14, 18, 27)
x = (2000, 2002, 2004, 2006, 2008)
plt.barh(x, C, color='tab:cyan', label='C')
plt.barh(x, B, color='tab:red', label='B')
plt.barh(x, A, color='tab:olive', label='A')
plt.title("Słupki poziome")
y=(0, 10, 20, 30, 40, 50, 60, 70, 80)
plt.xticks(y, color='tab:pink')
plt.yticks(color='tab:cyan')
plt.legend()
plt.savefig("zad1.pdf")
plt.show()
# zad2
df = pd.read_excel("transport32.xlsx")
print(df)
z = df.loc[df['Rodzaje pojazdów'] == 'samochody ciężarowe']
print(z)
x1 = z['Rok']
y1 = z['Wartość']
plt.plot(x1, y1, color='navy', linewidth=1.166, linestyle='--')
plt.title("Samochody ciężarowe")
plt.xlabel("Rok")
plt.ylabel("Wartość")
plt.grid()
plt.annotate(xy=(2011, 2767666), text='Szymon')
plt.savefig('zad2.png')
plt.show()
# zad3
df2=pd.read_excel("gastronomia32.xlsx")
df2=df2.transpose()
print(df2)
