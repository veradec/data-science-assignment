import matplotlib.pyplot as plt

x = [15, 3, 9, 25, 18, 7, 30, 12]
y = [30, 5, 12, 28, 20, 8, 40, 18]

plt.plot(x, y, 'r-h')
plt.xlabel('Input Values')
plt.ylabel('Output Values')
plt.title('Creative Line Plot')
plt.savefig('my_custom_plot.png')
plt.show()
