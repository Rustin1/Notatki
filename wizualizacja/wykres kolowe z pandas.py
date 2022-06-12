import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#1
df = pd.read_csv('cechy32.csv',sep=';')
#2
df = df.dropna()
#3
kroki = [100,120,140,160,180,200]
df['bin1']=pd.cut(df['Cecha1'],bins=kroki)
df['bin2']=pd.cut(df['Cecha2'],bins=kroki)
df.bin1 = df.bin1.astype('string')
df.bin2 = df.bin2.astype('string')
#4
fig, axs = plt.subplots(2,2)
fig.set_figwidth(13)
fig.set_figheight(13)
fig.delaxes(axs[0,1])
fig.delaxes(axs[1,0])

labels = list(df.bin1.unique())
labels = labels[:-1]
labels.sort()
#print(labels)


x1 = df.bin1.value_counts()
print(x1)
order1=[0,2,1,3,4]
labels1=[]
for i in order1:
  labels1.append(labels[i])

x2 = df.bin2.value_counts()
order2=[2,1,3,4,0]
labels2=[]
for i in order2:
  labels2.append(labels[i])


axs[0,0].pie(x1,explode=[0.1,0.1,0.1,0.1,0.1],labels=labels1, shadow=True, autopct='%1.1f%%')
axs[0,0].set_title('Cecha 1')
axs[1,1].pie(x2,explode=[0.1,0.1,0.1,0.1,0.1],labels=labels2, shadow=True, autopct='%1.1f%%')
axs[1,1].set_title('Cecha 2')



df.head()
plt.show()
