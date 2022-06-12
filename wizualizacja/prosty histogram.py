from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = [1,1,2,3,4,5,6,7,8,9,1,5,2,6,1]
plt.hist(x,bins=4)
plt.show()
