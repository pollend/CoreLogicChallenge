import srtm
import numpy as np
from mpl_toolkits.mplot3d import proj3d
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm

elevation_data = srtm.get_data()
fig = plt.figure()
ax = fig.gca(projection='3d')

def elevation(lat,lng):
    return float(elevation_data.get_elevation(lat,lng))


def obstruction(lat,lng):
    target_ele = elevation(lat,lng)
    itr = 101
    
    north = np.linspace(lat,lat+0.003, itr)
    eleN = []
    south = np.linspace(lat-0.003,lat, itr)
    eleS = []
    east = np.linspace(lng,lng+0.003, itr)
    eleE = []
    west = np.linspace(lng-0.003,lng, itr)
    eleW = []

    north = np.delete(north,[0])
    south = np.delete(south,[itr-1])

    east = np.delete(east,[0])
    west = np.delete(west,[itr-1])

    itr = itr-1

    eleNE = []
    eleNW = []
    eleSE = []
    eleSW = []

    basic_lat = np.linspace(lat,lat,itr)
    basic_lng = np.linspace(lng,lng,itr)

    # north elevations
    for i in range(itr):
        ele = elevation_data.get_elevation(north[i],basic_lng[i])
        if(ele is not None):
            eleN.append(ele)
        else:
            eleN.append(0)

    eleN = [target_ele - x for x in eleN]
    obsN =  all(i >= 0 for i in eleN)
    if obsN == True:
        print "North     : No obstruction"
    else:
        print "North: Obstruction"
        
    # south elevations
    for i in range(itr):
        ele = elevation_data.get_elevation(south[i],basic_lng[i])
        if(ele is not None):
            eleS.append(ele)
        else:
            eleS.append(0)

    eleS = [target_ele - x for x in eleS]
    obsS =  all(i >= 0 for i in eleS)
    if obsS == True:
        print "South: No obstruction"
    else:
        print "South: Obstruction"
        
    # east elevations
    for i in range(itr):
        ele = elevation_data.get_elevation(basic_lat[i],east[i])
        if(ele is not None):
            eleE.append(ele)
        else:
            eleE.append(0)

    eleE = [target_ele - x for x in eleE]
    obsE =  all(i >= 0 for i in eleE)
    if obsE == True:
        print "East: No obstruction"
    else:
        print "East: Obstruction"

    # west elevations
    for i in range(itr):
        ele = elevation_data.get_elevation(basic_lat[i],west[i])
        if(ele is not None):
            eleW.append(ele)
        else:
            eleW.append(0)

    eleW = [target_ele - x for x in eleW]
    obsW =  all(i >= 0 for i in eleW)
    if obsW == True:
        print "West: No obstruction"
    else:
        print "West: Obstruction"
        
    # north-east elevations
    for i in range(itr):
        ele = elevation_data.get_elevation(north[i],east[i])
        if(ele is not None):
            eleNE.append(ele)
        else:
            eleNE.append(0)

    eleNE = [target_ele - x for x in eleNE]
    obsNE =  all(i >= 0 for i in eleNE)
    if obsN == True:
        print "North-East: No obstruction"
    else:
        print "North-East: Obstruction"
        
    # south-east elevations
    for i in range(itr):
        ele = elevation_data.get_elevation(south[i],east[i])
        if(ele is not None):
            eleSE.append(ele)
        else:
            eleSE.append(0)

    eleSE = [target_ele - x for x in eleSE]
    obsSE =  all(i >= 0 for i in eleSE)
    if obsSE == True:
        print "South-East: No obstruction"
    else:
        print "South-East: Obstruction"
        
    # north-west elevations
    for i in range(itr):
        ele = elevation_data.get_elevation(north[i],west[i])
        if(ele is not None):
            eleNW.append(ele)
        else:
            eleNW.append(0)

    eleNW = [target_ele - x for x in eleNW]
    obsNW =  all(i >= 0 for i in eleNW)
    if obsNW == True:
        print "North-West: No obstruction"
    else:
        print "North-West: Obstruction"
        
    # south-west elevations
    for i in range(itr):
        ele = elevation_data.get_elevation(south[i],west[i])
        if(ele is not None):
            eleSW.append(ele)
        else:
            eleSW.append(0)

    eleSW = [target_ele - x for x in eleSW]
    obsSW =  all(i >= 0 for i in eleSW)
    if obsSW == True:
        print "South-West: No obstruction"
    else:
        print "South-West: Obstruction"
        
def heightMap(lat,lng):
    iterations = 20

    xr = np.linspace(lat-0.005,lat+0.005, iterations)
    yr = np.linspace(lng-0.005,lng+0.005, iterations)
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

    ax.scatter(lat, lng, elevation_data.get_elevation(lat,lng), c=[1,0,0])

    ax.plot_surface(X, Y, Z, rstride=8, cstride=8, alpha=0.3)
    cset = ax.contourf(X, Y, Z, zdir='z', offset=0, cmap=cm.coolwarm)
    # cset = ax.contourf(X, Y, Z, zdir='x', offset=(lat-5), cmap=cm.coolwarm)
    # cset = ax.contourf(X, Y, Z, zdir='y', offset=(longitude+5), cmap=cm.coolwarm)

    a = Arrow3D([lat + .006, lat + .006], [lng, lng + .003], [0,0], mutation_scale=20, lw=3, arrowstyle="-|>", color="r")
    ax.add_artist(a)
    
    ax.set_xlabel('latitude')
    ax.set_xlim(lat-0.005, lat+0.005)
    ax.set_ylabel('longitude')
    ax.set_ylim(lng-0.005,lng+0.005)
    ax.set_zlabel('elevation')
    #ax.set_zlim(0, 100)
    plt.show()

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)

def demo(lat,lng):
    print "Elevation:" , elevation(lat,lng) , "m"
    obstruction(lat,lng)
    heightMap(lat,lng)

demo(32.8721,-117.249)
    
