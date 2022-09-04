import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dane = pd.read_csv("sport1.csv", sep="_")
m = dane[dane["Płeć"]=="M"]
k = dane[dane["Płeć"]=="K"]
et = m["Sport"]
plt.subplot(2, 1, 1)
plt.title("Mężczyźni")
plt.pie(m["Popularność"], autopct='%1.0f%%', labels=et, startangle=30)
plt.subplot(2, 1, 2)
plt.title("Kobiety")
plt.pie(k["Popularność"], autopct='%1.0f%%', labels=et)
plt.tight_layout()
plt.savefig("zad3.jpg")
plt.show()