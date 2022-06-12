from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fig,ax = plt.subplots(1)

data = [[30,25,50,20],
        [40,20,35,10],
        [1,3,7,24]]
X = np.arange(4)

ax.barh(X + 0.00, data[0], color = "b",height=0.25, label="A")
ax.barh(X + 0.25, data[1], color = "r",height=0.25, label="B")
ax.barh(X + 0.50, data[2], color = "g",height=0.25, label="C")
labelsbar = np.arange(2015,2019)
plt.yticks(X+0.25,labelsbar)
ax.invert_xaxis()
ax.invert_yaxis()
plt.legend()
plt.show()
