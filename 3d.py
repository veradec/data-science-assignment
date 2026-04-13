import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 3, 5, 7])
y = np.array([9, 1, 7, 4])
plt.subplot(2, 1, 1)
plt.plot(x, y, 'm-')

x = np.array([1, 3, 5, 7])
y = np.array([25, 35, 45, 55])
plt.subplot(2, 1, 2)
plt.plot(x, y, 'c*')

plt.show()
