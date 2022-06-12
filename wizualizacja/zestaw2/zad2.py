csv = pd.read_csv('ceny3.csv',sep='#',decimal=',')
df = pd.DataFrame(csv)

print(df)


j = df.loc[df["Rodzaje towarów i usług"]== "ryż - za 1kg"]
d = df.loc[df["Rodzaje towarów i usług"]== "mąka pszenna - za 1kg"]


cenaj = j["Wartosc"]
miesiacj = j['Miesiące']
cenad = d["Wartosc"]
miesiacd = d['Miesiące']

print("ryż - za 1kg", j["Wartosc"].mean())
print("mąka pszenna - za 1kg", d["Wartosc"].mean())

fig,[ax1,ax2]=plt.subplots(1,2)

ax1.plot(miesiacj, cenaj, ls='--' ,label='ryz', color = "red")
ax1.set_xticks(miesiacj)
ax1.set_yticks(cenaj)
ax2.plot(miesiacd, cenad, ls='--' ,label='pszenica', color = "red")
ax2.set_xticks(miesiacj)
ax2.set_yticks(cenad)
ax1.set_xticklabels(labels = miesiacj, rotation=45, fontsize=6)
ax2.set_xticklabels(labels = miesiacd, rotation=45, fontsize=6)
plt.figtext(0.02, 0, '166324', size=12, color='k')

plt.show()
