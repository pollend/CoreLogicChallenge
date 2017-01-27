import srtm
import numpy as np
from mpl_toolkits.mplot3d import proj3d
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
import googlemaps,json
gmaps = googlemaps.Client(key='AIzaSyBkFhUMEuDdlSBXYp18Pmy7bMKwK0M7IrM')

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
        print 'North:'.ljust(12), "No obstruction"
    else:
        print 'North:'.ljust(12), "Obstruction"
        
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
        print 'South:'.ljust(12), "No obstruction"
    else:
        print 'South:'.ljust(12), "No obstruction"
        
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
        print 'East:'.ljust(12), "No obstruction"
    else:
        print 'East:'.ljust(12), "Obstruction"

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
        print 'West:'.ljust(12), "No obstruction"
    else:
        print 'West:'.ljust(12), "Obstruction"
        
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
        print 'North-East:'.ljust(12), "No obstruction"
    else:
        print 'North-East:'.ljust(12), "Obstruction"
        
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
        print 'South-East:'.ljust(12), "No obstruction"
    else:
        print 'South-East:'.ljust(12), "Obstruction"
        
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
        print 'North-West:'.ljust(12), "No obstruction"
    else:
        print 'North-West:'.ljust(12), "Obstruction"
        
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
        print 'South-West:'.ljust(12), "No obstruction"
    else:
        print 'South-West:'.ljust(12), "Obstruction"
        
class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)


      
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

    ax.add_artist(Arrow3D([lat + .006, lat + .006], [lng, lng + .003], [0,0], mutation_scale=20, lw=3, arrowstyle="-|>", color="r"))

    ax.ticklabel_format(useOffset=False)

    ax.set_xlabel('latitude')
    ax.set_xlim([lat-0.005, lat+0.005])
    ax.set_ylabel('longitude')
    ax.set_ylim([lng-0.005,lng+0.005])
    ax.set_zlabel('Elevation (m)')
    plt.show()


def statsCoord(lat,lng):
    m = elevation(lat,lng)
    print "Elevation:" , m , "m /",m*3.28084,"ft"
    obstruction(lat,lng)
    heightMap(lat,lng)

def statsAddr(addr):
    geocode_result = gmaps.geocode(addr)
    lat = geocode_result[0]['geometry']['location']['lat']
    lng = geocode_result[0]['geometry']['location']['lng']
    statsCoord(lat,lng)

def demo(instanceOf,*args):
    if instanceOf == 'coord':
        statsCoord(args[0],args[1])
    if instanceOf == 'addr':
        statsAddr(args[0])
    


    
