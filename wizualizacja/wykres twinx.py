from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fig, ax1 = plt.subplots()
x = np.arange(0.01, 10.0, 0.01)
y = x**2
ax1.plot(x,y,'r')
ax2=ax1.twinx()
y2=np.sin(x)
ax2.plot(x,y2)
fig.tight_layout()
plt.show()

