from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fig, ax1 = plt.subplots()
t = np.arange(0.01, 10.0, 0.01)
s1 = np.exp(t)
ax1.plot(t,s1,'black')
ax1.set_xlabel('time (s)')

ax1.set_ylabel('exp', color='black')
ax1.tick_params('y', colors='black')

ax2 = ax1.twinx()
s2 = np.sin(2 * np.pi * t)
ax2.plot(t, s2, 'r.')
ax2.set_ylabel('sin', color='r')
ax2.tick_params('y', colors='r')
fig.tight_layout()
plt.show()
