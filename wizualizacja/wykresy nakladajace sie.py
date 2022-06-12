from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

N = 5
boys = {20,30,40,50,60}
girls = {25,35,45,55,65}
ind = np.arange(N)
width = 0.5

plt.bar(ind, boys, width, label = "boys")
plt.bar(ind, girls, width,bottom=boys, label = "girls") #bottom sprawia ze wykres leci od danego miejsca

plt.ylabel('Contribution')
plt.title('Contribution by the team')
plt.xticks(ind, ('T1','T2','T3','T4','T5'))
plt.yticks(np.arange(0,125,10))
plt.legend()
plt.show()
