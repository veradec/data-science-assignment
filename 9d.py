import matplotlib.pyplot as plt

plt.plot([10, 20, 30, 40], [100, 250, 200, 400], 'm-o')
plt.xticks([10, 20, 30, 40], ['Low', 'Med', 'High', 'Max'])
plt.yticks([100, 200, 300, 400], ['Min', 'Avg', 'Good', 'Peak'])
plt.show()
