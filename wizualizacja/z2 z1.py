import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
plt.rcdefaults()
fig, ax = plt.subplots(1,2)

# Example data
literki = ('E', 'D', 'C', 'B', 'A')
y_pos = np.arange(len(literki))
performance = (40,41,15,45,35)
performance2 = (-30,-32.5,-35,-32,-30)
#error = np.random.rand(len(literki))
colors = ['purple','grey','darkorange','pink','skyblue']
colors2 = ['yellowgreen','saddlebrown','c','c','magenta']

ax[0].barh(y_pos, performance, align='center', color = colors)
ax[0].set_yticks(y_pos, labels=literki)
ax[0].invert_yaxis()  # labels read top-to-bottom
ax[0].set_title('Wykres lewy')

ax[1].barh(y_pos, performance2, align='center', color = colors2)
ax[1].set_yticks(y_pos, labels=literki)
ax[1].invert_yaxis()  # labels read top-to-bottom
ax[1].set_title('Wykres prawy')

plt.show()
