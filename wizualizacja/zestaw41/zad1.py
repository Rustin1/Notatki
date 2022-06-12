import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x = np.linspace(0.5,10)
fun1 = np.log10(x)
fun2 = -4*x+2
fun3 = 2*np.cos(x)
fig, ax = plt.subplots()
#https://matplotlib.org/3.5.0/tutorials/intermediate/legend_guide.html
line1, = ax.plot(x, fun1, 'b--', label = 'Funkcja 1')
line2, = ax.plot(x, fun2, 'r-.', label = 'Funkcja 2')
line3, = ax.plot(x, fun3, 'g*', label = 'Funkcja 3')
ax.set_title('Wykres zad1')
ax.legend(handles=[line1, line3, line2],loc="right")
ax.set_xlabel('Oś x')
ax.set_ylabel('Oś y')
ax.grid()
#fig.savefig('zad1.png')
plt.show()
