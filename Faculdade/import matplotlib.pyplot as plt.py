import matplotlib.pyplot as plt
import numpy as np

omega = 2
z_line=np.linspace(0,10,100)
x_line=np.cos(omega*z_line)
y_line=np.sin(omega*z_line)
ax = plt.axes(projection = '3d')
ax.plot3D(x_line,y_line,z_line)
# plt.figure(figsize=(20,20))
plt.show()