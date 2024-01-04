# hello.py

print("Hello, World!")


import matplotlib.pyplot as plt
import numpy as np

# x = np.linspace(0, 2 * np.pi, 200)
# y = np.sin(x)

# plt.plot(x, y)

incomes = np.random.normal(100.0, 20.0, 10000)

median = np.median(incomes)

print ("the median is ", median)

plt.hist(incomes, 50)


plt.savefig('plot.png')  # saves the plot as 'plot.png' in the current directory 