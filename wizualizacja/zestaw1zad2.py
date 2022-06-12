import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import openpyxl
#zadanie2
xlsx = pd.ExcelFile('ceny1.xlsx')
df=pd.read_excel(xlsx, header=0)
df=pd.DataFrame(df)
grupa=df.groupby('Rok').agg({'Wartość':['sum']})
print(df)
grupa.plot(xlabel='Wartość', ylabel='Rok', title='Wartość produktów przez lata', color='green', marker='.')
plt.legend(['Cena produktów przez lata'])
plt.savefig('164343.png')
plt.show()
