from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

width=[3,-16,5,20,40]
bars = ('A','B','C','D','E')
x_pos=np.arange(len(bars))
plt.barh(x_pos,width,color=['black','yellow','blue','red','pink'])
plt.yticks(x_pos,bars)
plt.show()
