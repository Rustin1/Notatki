from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(123)
df = pd.DataFrame(np.random.rand(10,4), columns=['a','b','c','d'])
df.plot.area()
plt.show()
