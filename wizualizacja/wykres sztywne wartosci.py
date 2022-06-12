from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = [[30,25,50,20],
        [40,20,35,10],
        [1,3,7,24]]
X = np.arange(4)

plt.bar(X + 0.00, data[0], color = "b", width=0.25, label="A")
plt.bar(X + 0.25, data[1], color = "r", width=0.25, label="B")
plt.bar(X + 0.50, data[2], color = "g", width=0.25, label="C")
labelsbar = np.arange(2015,2019)
plt.xticks(X+0.25,labelsbar)
plt.legend()
plt.show()
