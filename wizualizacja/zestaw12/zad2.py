import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#1
df = pd.read_excel('sprzedaz12.xlsx')
#2
dfg = df.groupby("Produkt")['Sprzedaż'].sum()
print(dfg)
#3
df2015 = df[df.Rok==2015]
df2016 = df[df.Rok==2016]
df2017 = df[df.Rok==2017]
fig, axs = plt.subplots(1,3)
fig.set_figheight(15)
fig.set_figwidth(15)
axs[0].pie(df2015['Sprzedaż'], explode=[0.1, 0.1, 0.1], labels=df2015['Produkt'], autopct='%1.1f%%', shadow=True)
axs[0].set_title('2015')
axs[1].pie(df2016['Sprzedaż'], explode=[0.1, 0.1, 0.1], labels=df2016['Produkt'], autopct='%1.1f%%', shadow=True)
axs[1].set_title('2016')
axs[2].pie(df2017['Sprzedaż'], explode=[0.1, 0.1, 0.1], labels=df2017['Produkt'], autopct='%1.1f%%', shadow=True)
axs[2].set_title('2017')
plt.show()
