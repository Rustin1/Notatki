import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#1
df = pd.read_excel('sprzedaz32.xlsx')
#2
dfg = df.groupby(["Produkt"])["Sprzedaż"].sum()
print(dfg)

#3
#https://stackoverflow.com/questions/47796264/how-to-create-a-grouped-bar-plot
df.pivot("Rok","Produkt","Sprzedaż").plot(kind="bar")
plt.text(x=3,y=2100,s="123456")
plt.legend()
print(df.pivot("Rok","Produkt","Sprzedaż"))
#df.head(10)
plt.show()
