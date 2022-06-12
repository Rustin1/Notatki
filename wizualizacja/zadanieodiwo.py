#zaciągamy dane
csv = pd.read_csv('nieruchomosci2.csv',sep=';',header=None)
df = pd.DataFrame(csv)
# dane={'Typ':[],'Rok':[],'ilosc sztuk':[]}
print(df)
# tutaj linijka z wartościami 
df.loc[3,:] = df.loc[3,:].str.replace(" ", "").astype(int)
df = df.transpose()

#Nazywamy kolumny
df.columns =['rynek', 'Metraz', 'Rok', 'ilosc']
print(df)
#wybieramy jaki typ wartości nas interesuje
grupa=df.where(df['rynek']=='rynek wtórny')
#Czy sumujemy czy Średnia
grupa=grupa.groupby('Metraz').agg({'ilosc':'sum'})

grupa.plot(kind='pie',subplots=True,autopct='%.2f %%',fontsize=10,figsize=(8,8))
plt.legend(title='metraż')
plt.title('wykres przedstawiający stosunek ilości mieszkań poszczególnych metraży sprzedanych w 2 roku')
plt.show()
#wybieramy jaki typ wartości nas interesuje
grupa=df.where(df['rynek']=='rynek pierwotny')
#Czy sumujemy czy Średnia
grupa=grupa.groupby('Metraz').agg({'ilosc':'sum'})
grupa.plot(kind='pie',subplots=True,autopct='%.2f %%',fontsize=10,figsize=(8,8))
plt.legend(title='metraż')
plt.title('wykres przedstawiający stosunek ilości mieszkań poszczególnych metraży sprzedanych w 2018 roku')
plt.show()
