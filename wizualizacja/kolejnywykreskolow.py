import matplotlib.pyplot as plt
import pandas as pd
import random
import numpy as np
import math
import seaborn as sns

labels=['LG','','PD','PD','','Pl']
color= ['orange','lightblue','azure','blue','green','red']
sizes=[18.07, 13.87, 14.71,17.23,19.33,16.81]
explode=[0.2, 0, 0, 0,0,0]
# fig1, ax1=plt.subplots()
plt.pie(sizes, explode=explode, labels=labels, autopct='%0.2f%%',shadow=False, startangle=70, colors=color)
plt.title("tytuł")
plt.show()
