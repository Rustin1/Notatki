import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import openpyxl
def f(x):
    return np.sin(x)
def g(x):
    return np.cos(x)/2
x=np.arange(0,5,0.1)
fig, ax1 = plt.subplots()
ax1.plot(x, f(x), linestyle='dotted', color='orange', label='sin(x)')
ax1.set_ylabel('oś lewa', color='green')
ax1.legend(loc='center right')
plt.ylim(bottom=-1,top=1)
ax2 = ax1.twinx()
ax2.plot(x, g(x), linestyle='dotted', color='brown', label='cos(x)')
ax2.set_ylabel('oś prawa', color='red')
ax2.legend(loc='lower center')
ax2.yaxis.set_label_coords(1.1,0.5)
plt.xlabel('oś dolna')
plt.title('To jest tytuł wykresu')
plt.ylim(bottom=-1,top=1)
plt.xlim(0,5)
plt.show()
