import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#1
df = pd.read_csv('cechy41.csv',sep=';', decimal=',')
df = df.dropna()
#2
kroki = [0,50,100,150,200]
df['bin1']=pd.cut(df['Cecha1'],bins=kroki)
df['bin2']=pd.cut(df['Cecha2'],bins=kroki)
df.bin1 = df.bin1.astype('string')
df.bin2 = df.bin2.astype('string')
#3
fig, axes = plt.subplots(1,2)
fig.set_figwidth(12)
fig.set_figheight(6)
#https://stackoverflow.com/questions/22483588/how-can-i-plot-separate-pandas-dataframes-as-subplots
df.bin1.value_counts().plot(kind='bar',ax=axes[1])
df.bin2.value_counts().plot(kind='bar',ax=axes[0])



df.dtypes
df.head()
plt.show()
