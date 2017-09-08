import matplotlib.pyplot as plt
import numpy as np

y1 = [46, 271,114,43,178,2,7,167,24,31,56,38,166,45,171,50,9,41,94,108,3]
y2 = [159,92,188,158,145,24,12,88,55,80,48,29,69,41,78,124,95,45,96,114,6]

x = np.arange(1990, 2011, 1)

fig, ax = plt.subplots()
rects1 = ax.bar(x, y1, 0.3, color='#87CEFA', alpha=0.8)
rects2 = ax.bar(x+0.3, y2, 0.3, color='#808080', alpha=0.8)

# add some text for labels, title and axes ticks
ax.set_title('台风个数统计')
ax.set_xlim([1989,2011])
# ax.set_xticks(ind + width / 2)
# ax.set_xticklabels(('G1', 'G2', 'G3', 'G4', 'G5'))

ax.legend((rects1[0], rects2[0]), ('预测', '观测'))
plt.show()
