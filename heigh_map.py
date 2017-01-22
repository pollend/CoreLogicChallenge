"""
.. versionadded:: 1.1.0
   This demo depends on new features added to contourf3d.
"""

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
import srtm
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')

elevation_data = srtm.get_data()

lat = 32.7983
longitude = -117.216



# x_axis = np.arange(lat-1,lat+1,0.1)
# y_axis = np.arange(longitude-1,longitude+1,0.1)

# X,Y = np.meshgrid(x_axis,y_axis, sparse=True)
# Z = np.sqrt (X * X + Y * Y) 

iterations = 500

xr = np.linspace(lat-0.005,lat+0.005, iterations)
yr = np.linspace(longitude-0.005,longitude+0.005, iterations)
print(xr)
X, Y = np.meshgrid(xr, yr)

zr = []
for i in range(0, iterations):
    for k in range(0, iterations):
        ele = elevation_data.get_elevation(xr[i],yr[k])
        if(ele is not None):
            zr.append(ele)
        else:
            zr.append(0)

Z = np.reshape(zr, X.shape)

ax.scatter(lat, longitude, elevation_data.get_elevation(lat,longitude), c=[1,0,0])

ax.plot_surface(X, Y, Z, rstride=8, cstride=8, alpha=0.3)
cset = ax.contourf(X, Y, Z, zdir='z', offset=0, cmap=cm.coolwarm)
# cset = ax.contourf(X, Y, Z, zdir='x', offset=(lat-5), cmap=cm.coolwarm)
# cset = ax.contourf(X, Y, Z, zdir='y', offset=(longitude+5), cmap=cm.coolwarm)

ax.set_xlabel('lat')
ax.set_xlim(lat-0.005, lat+0.005)
ax.set_ylabel('long')
ax.set_ylim(longitude-0.005,longitude+0.005)
# ax.set_zlabel('Z')
# ax.set_zlim(0, 100)

plt.show()
