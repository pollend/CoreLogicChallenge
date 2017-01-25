"""
.. versionadded:: 1.1.0
   This demo depends on new features added to contourf3d.
"""

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
import srtm
import numpy as np
from mpl_toolkits.mplot3d import proj3d
from matplotlib.patches import FancyArrowPatch

fig = plt.figure()
ax = fig.gca(projection='3d')

elevation_data = srtm.get_data()

lat = 32.7983
longitude = -117.216


class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)



# x_axis = np.arange(lat-1,lat+1,0.1)
# y_axis = np.arange(longitude-1,longitude+1,0.1)

# X,Y = np.meshgrid(x_axis,y_axis, sparse=True)
# Z = np.sqrt (X * X + Y * Y) 
iterations = 20

xr = np.linspace(lat-0.005,lat+0.005, iterations)
yr = np.linspace(longitude-0.005,longitude+0.005, iterations)
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

a = Arrow3D([lat + .006, lat + .006], [longitude, longitude + .003], [0,0], mutation_scale=20, lw=3, arrowstyle="-|>", color="r")
ax.add_artist(a)


ax.set_xlabel('latitude')
ax.set_xlim(lat-0.005, lat+0.005)
ax.set_ylabel('longitude')
ax.set_ylim(longitude-0.005,longitude+0.005)
ax.set_zlabel('elevation')
#ax.set_zlim(0, 100)

plt.show()
