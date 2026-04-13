import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 2, 4, 6])
y = np.array([5, 15, 10, 25])
plt.subplot(1, 2, 1)
plt.plot(x, y, 'r--')

x = np.array([0, 2, 4, 6])
y = np.array([100, 50, 200, 150])
plt.subplot(1, 2, 2)
plt.plot(x, y, 'g^')

plt.show()
