import matplotlib.pyplot as plt
labels = ['A','B','C','D','E']
values = [-50,-15,-24,-27,-47]
values.reverse()
#https://i.stack.imgur.com/lFZum.png
plt.barh(labels,values,color=['goldenrod','saddlebrown','mediumslateblue','firebrick','dodgerblue'])
plt.show()
