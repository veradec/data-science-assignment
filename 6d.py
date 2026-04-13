import matplotlib.pyplot as plt

fig, axs = plt.subplots(2, 2)

axs[0, 0].plot([5, 15, 25], [50, 150, 100], 'r-o')
axs[0, 1].scatter([2, 4, 6, 8], [12, 18, 24, 30], c='purple', s=80)
axs[1, 0].bar(['A', 'B', 'C'], [7, 14, 21], color='orange')
axs[1, 1].hist([5, 5, 5, 10, 10, 15, 20, 20, 20, 20, 25, 30, 30], bins=5, color='green')

plt.show()
