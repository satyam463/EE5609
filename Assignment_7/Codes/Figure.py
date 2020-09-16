import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5,5,100)
y_1 = (3*x+5)/4          # Line 1
y_2 = (7-2*x)/3          # Line 2

plt.plot(x, y_1, 'blue', label='3x-4y+5=0')
plt.plot(x, y_2, 'green', label='2x+3y-7=0')

plt.xlabel('X - Axis', color='black')
plt.ylabel('Y - Axis', color='black')
plt.legend(loc='upper center')
plt.grid()

plt.show()
