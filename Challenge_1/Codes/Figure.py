import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
fig.set_size_inches(10,10)
ax = fig.add_subplot(111, projection='3d')

#Two Points on Line 1 with k_1=-2 and k_1=3
x_1=np.array([-1,4])
y_1=np.array([8,-7])
z_1=np.array([-1,9])

#Two Points on Line 2 with k_2=-2 and k_2=0 
x_2=np.array([0,4])
y_2=np.array([-1,5])
z_2=np.array([4,6])

ax.plot(x_1,y_1,z_1,color='blue',label='line_1')
ax.plot(x_2,y_2,z_2,color='red',label='line 2')

# Solved Points on the lines
x_pq = np.array([29/19,20/19])
y_pq = np.array([8/19,11/19])
z_pq = np.array([77/19,86/19])

ax.text(x_pq[0], y_pq[0], z_pq[0], "P")
ax.text(x_pq[1], y_pq[1], z_pq[1], "Q")

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

ax.scatter(x_pq,y_pq,z_pq, c = "green")

plt.show()
