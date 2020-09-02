import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
from mpl_toolkits import mplot3d

ax = plt.axes(projection='3d')

# Coordinates
x_s = [0,5]
y_s = [0,-2]
z_s = [0,3]

#Plot
plot, = ax.plot3D(x_s, y_s, z_s, label = "Line Pasing through Origin and P(5,-2,3)")
plt.legend(handles=[plot])
