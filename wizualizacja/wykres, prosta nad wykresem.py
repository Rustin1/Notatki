import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

labels = ['A','B','C','D','E']
valbar = [21,41,21,37,49]
valline = [69,55,72,65,55]
#https://i.stack.imgur.com/lFZum.png
fig, ax = plt.subplots()
fig.set_figwidth(10)
fig.set_figheight(7)
ax.plot(labels,valline,':',linewidth=2)
ax.bar(labels,valbar,color=['y','saddlebrown','orchid','c','orchid'])
ax.set_title('Wykres',fontsize=16)
ax.tick_params(axis='x',labelsize=13)
ax.tick_params(axis='y',labelsize=13)
plt.show()
