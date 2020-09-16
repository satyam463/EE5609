import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5,5,100)
y_1 = (2*x+7)/3          # Line 1
y_2 = (20-12*x)/5        # Line 2

plt.plot(x, y_1, 'blue', label='2X-3y+7=0')
plt.plot(x, y_2, 'green', label='12X+5y-20=0')

plt.xlabel('X - Axis', color='black')
plt.ylabel('Y - Axis', color='black')
plt.legend(loc='best')
plt.grid()

plt.show()
