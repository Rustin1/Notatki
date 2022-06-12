import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#1
df = pd.read_excel('ceny41.xlsx')
#2
dfg = df.groupby('Rodzaje towarów i usług')['Wartosc'].mean()
#print(dfg)

#3
x = df.Miesiące.unique()
produkty = df['Rodzaje towarów i usług'].unique()
fig, ax = plt.subplots()
for i in produkty:
  tmp = df[df['Rodzaje towarów i usług']==i]
  ax.plot(x,tmp.Wartosc)
#https://stackabuse.com/rotate-axis-labels-in-matplotlib/
ax.tick_params(axis='x',labelrotation=90)
ax.text(x=0,y=1,s='123456')
df.head()
plt.show()
