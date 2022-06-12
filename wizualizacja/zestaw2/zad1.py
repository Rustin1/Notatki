from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
fig,axes=plt.subplots(1,2)
width2=[3,16,5,20,40]
width3=[-40,-30,-10,-20,-25]
bars = ('A','B','C','D','E')
x_pos=np.arange(len(bars))
axes[0].barh(bars,width2,color=['blue','pink','orange','grey','purple'])
axes[0].title.set_text('First Plot')
plt.title("wykres lewy")
axes[1].barh(bars,width3,color=['magenta','blue','blue','brown','yellow',])
axes[1].title.set_text('second Plot') # dodanie tytulu do subplota
plt.yticks(x_pos,bars)
plt.show()
