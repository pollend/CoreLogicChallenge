
import srtm
import numpy as np

elevation_data = srtm.get_data()

itr = 20
lat = 32.8721
lng = -117.249

north = np.linspace(lat,lat+0.005, itr)
eleN = []
south = np.linspace(lat-0.005,lat, itr)
eleS = []
east = np.linspace(lng,lng+0.005, itr)
eleE = []
west = np.linspace(lng-0.005,lng, itr)
eleW = []

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

# south elevations
for i in range(itr):
    ele = elevation_data.get_elevation(south[i],basic_lng[i])
    if(ele is not None):
        eleS.append(ele)
    else:
        eleS.append(0)

# east elevations
for i in range(itr):
    ele = elevation_data.get_elevation(basic_lat[i],east[i])
    if(ele is not None):
        eleE.append(ele)
    else:
        eleE.append(0)

# west elevations
for i in range(itr):
    ele = elevation_data.get_elevation(basic_lat[i],west[i])
    if(ele is not None):
        eleW.append(ele)
    else:
        eleW.append(0)


print eleN
print eleS
print eleE
print eleW
