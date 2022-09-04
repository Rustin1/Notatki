import numpy as np
import matplotlib.pyplot as plt

fig, ax1 = plt.subplots()
x= np.arange(0, 10.0, 0.01)
y = x+4
ax1.plot(x, y, linestyle='dashed', color="orange", label="y=x+4")
ax1.set_title("Wykresy dwóch funkcji liniowych")
plt.legend()
plt.grid()
ax1.set_ylabel('oś pionowa po lewej stronie', color='green')
ax1.set_xlabel('oś pozioma', color='pink')
ax2= ax1.twinx()
y2 = -x-6
ax2.plot(x, y2, linestyle='dashdot', color="brown", label="y=-x-6")
plt.legend()
ax1.set_ylabel('oś pionowa po prawej stronie', color='brown')
fig.tight_layout()
plt.savefig("zad1.png")
plt.show()