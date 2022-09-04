import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
dane = pd.read_excel ("linieautobusowe10.xlsx")
plt.scatter(dane[ "Rok"],dane["Wartosc"], marker="<", color="red", label="Wartość")
plt.annotate(xy=[2014, 11500], text="123456")
plt.legend()
plt.title("Dane o liniach autobusowych w Polsce")
plt.xlabel("Lata")
plt.xticks(dane [ "Rok"])
plt.ylabel("szt.")
plt.tight_layout()
plt.grid()
plt.savefig("zad2.jpg")
plt.show()