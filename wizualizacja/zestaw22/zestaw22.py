import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib.pyplot as plt
import numpy as np

# # Fixing random state for reproducibility
# # #Zad_1
# plt.plot((np.arange(0,math.pi*3,0.1)),(np.arange(0,math.pi*3,0.1)+math.e),color='blue',linestyle='--')
# plt.plot((np.arange(0,math.pi*3,0.1)),(-4*np.arange(0,math.pi*3,0.1)+2),color='red',linestyle='-.')
# plt.plot((np.arange(0,math.pi*3,0.1)),(2*np.cos(np.arange(0,math.pi*3,0.1))),color='green',linestyle=':')
# plt.grid()
# plt.xticks(np.arange(-1,11,1))
# plt.xlabel('os X')
# plt.ylabel('os y')
# plt.legend(labels=['log(2x)', '2cos(x)','-4x+2'],loc="best")
# plt.savefig('obrazek.png')
# plt.show()
#
# # Zad_2
# xlsx = pd.read_excel('mieszkania22.xlsx')
# df = pd.DataFrame(xlsx)
# print(df)
# j = df.loc[df["Formy budownictwa"]== "indywidualne"]
# p = df.loc[df["Formy budownictwa"]== "spółdzielcze"]
# c = df.loc[df["Formy budownictwa"]== "komunalne"]
# cenar  = j["Wartość"]
# miesiacr = j["Rok"]
# cenam  = p["Wartość"]
# miesiacm = p["Rok"]
# cenac  = c["Wartość"]
# miesiacc = c["Rok"]
#
# print("indywidualne ", j["Wartość"].mean())
# print("spółdzielcze ", p["Wartość"].mean())
# print("komunalne ", p["Wartość"].mean())
#
# plt.bar(miesiacr, cenar, ls='--' ,label='indywidualne', color = "red",width=0.25)
# plt.bar(miesiacm+0.25, cenam, ls='-.' ,label='spółdzielcze', color = "orange",width=0.25)
# plt.bar(miesiacc+0.5, cenac, ls='-.' ,label='komunalne', color = "yellow",width=0.25)
# plt.xlabel("Rok")
# plt.xticks(np.arange(2015,2019),rotation=45)
# plt.ylabel("Ceny w zł")
# plt.figtext(0.02, 0.95, '166324', size=12, color='k')
# plt.grid(axis='y')
# plt.legend(loc='best')
# plt.title("Cena za mieszkanie")
# plt.savefig("excel.jpg")
# plt.show()
#
# #Zad_3
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
# #Zad_1
plt.plot((np.arange(0,np.pi*3,0.1)),(np.arange(0,math.pi*3,0.1)+math.e),color='blue',linestyle='--')
plt.plot((np.arange(0,np.pi*3,0.1)),(-4*np.arange(0,math.pi*3,0.1)+2),color='red',linestyle='-.')
plt.plot((np.arange(0,np.pi*3,0.1)),(2*np.cos(np.arange(0,math.pi*3,0.1))),color='green',linestyle=':')
plt.grid()
plt.xticks(np.arange(-1,11,1))
plt.xlabel('os X')
plt.ylabel('os y')
plt.legend(labels=['log(2x)', '2cos(x)','-4x+2'],loc="best")
plt.savefig('obrazek.png')
plt.show()

# Zad_2
xlsx = pd.read_excel('mieszkania22.xlsx')
df = pd.DataFrame(xlsx)
print(df)
j = df.loc[df["Formy budownictwa"]== "indywidualne"]
p = df.loc[df["Formy budownictwa"]== "spółdzielcze"]
c = df.loc[df["Formy budownictwa"]== "komunalne"]
cenar  = j["Wartość"]
miesiacr = j["Rok"]
cenam  = p["Wartość"]
miesiacm = p["Rok"]
cenac  = c["Wartość"]
miesiacc = c["Rok"]

print("indywidualne ", j["Wartość"].mean())
print("spółdzielcze ", p["Wartość"].mean())
print("komunalne ", p["Wartość"].mean())
plt.bar(miesiacr, cenar, ls='--' ,label='indywidualne', color = "red",width=0.25)
plt.bar(miesiacm+0.25, cenam, ls='-.' ,label='spółdzielcze', color = "orange",width=0.25)
plt.bar(miesiacc+0.5, cenac, ls='-.' ,label='komunalne', color = "yellow",width=0.25)
plt.xlabel("Rok")
plt.xticks(np.arange(2015,2019),rotation=45)
plt.ylabel("Ceny w zł")
plt.figtext(0.02, 0.95, '166324', size=12, color='k')
plt.grid(axis='y')
plt.legend(loc='best')
plt.title("Cena za mieszkanie")
plt.savefig("excel.jpg")
plt.show()

#Zad_3

csv = pd.read_csv('transport22.csv',sep=';',header=None)
df = pd.DataFrame(csv)
dane={'Typ':[],'Rok':[],'ilosc sztuk':[]}
print(df)
df.loc[3,:] = df.loc[3,:].str.replace(" ", "").astype(int)
df = df.transpose()


df.columns =['typ', 'Rok', 'Ilość w szt', 'ilość']
print(df)
grupa=df.where(df['Rok']=='2010')
grupa=grupa.groupby('typ').agg({'ilość':'sum'})

grupa.plot(kind='pie',subplots=True,autopct='%.2f %%',fontsize=10,figsize=(8,8))
plt.legend(title='metraż')
plt.title('wykres przedstawiający stosunek ilości mieszkań poszczególnych metraży sprzedanych w 2 roku')
plt.show()

grupa=df.where(df['Rok']=='2015')
grupa=grupa.groupby('typ').agg({'ilość':'sum'})
grupa.plot(kind='pie',subplots=True,autopct='%.2f %%',fontsize=10,figsize=(8,8))
plt.legend(title='metraż')
plt.title('wykres przedstawiający stosunek ilości mieszkań poszczególnych metraży sprzedanych w 2018 roku')
plt.show()

