import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('dosw12.csv',sep=';')
df = df.dropna() # usuniecie pustych wynikow
fig, ax = plt.subplots(figsize=(8,8))
ax.plot(df.Czas, df.Zmienna1, '--')
ax.plot(df.Czas, df.Zmienna2)
ax.plot(df.Czas, df.Zmienna3, '.')
#https://jakevdp.github.io/PythonDataScienceHandbook/04.10-customizing-ticks.html
#ax.xaxis.set_major_locator(plt.MaxNLocator(21))
#ax.yaxis.set_major_locator(plt.MaxNLocator(50))
ax.xaxis.set_major_locator(plt.MaxNLocator(21))
ax.yaxis.set_major_locator(plt.MaxNLocator(50))
plt.show()
