
import srtm
import math
import MySQLdb
import sys
import numpy as np

elevation_data = srtm.get_data()
##
##latv = 32.8721
##lngv = -117.249
##
##itrv = 101 # add a 1 to ensure that divisions are in degree of 10s later

def directionalElevation(lat,lng,itr):
        
    north = np.linspace(lat,lat+0.005, itr)
    eleN = []
    south = np.linspace(lat-0.005,lat, itr)
    eleS = []
    east = np.linspace(lng,lng+0.005, itr)
    eleE = []
    west = np.linspace(lng-0.005,lng, itr)
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


    # north-east elevations
    for i in range(itr):
        ele = elevation_data.get_elevation(north[i],east[i])
        if(ele is not None):
            eleNE.append(ele)
        else:
            eleNE.append(0)

    # south-east elevations
    for i in range(itr):
        ele = elevation_data.get_elevation(south[i],east[i])
        if(ele is not None):
            eleSE.append(ele)
        else:
            eleSE.append(0)

    # north-west elevations
    for i in range(itr):
        ele = elevation_data.get_elevation(north[i],west[i])
        if(ele is not None):
            eleNW.append(ele)
        else:
            eleNW.append(0)

    # south-west elevations
    for i in range(itr):
        ele = elevation_data.get_elevation(south[i],west[i])
        if(ele is not None):
            eleSW.append(ele)
        else:
            eleSW.append(0)

    n = math.ceil(np.mean(eleN)*100)/100
    s = math.ceil(np.mean(eleS)*100)/100
    e = math.ceil(np.mean(eleE)*100)/100
    w = math.ceil(np.mean(eleW)*100)/100
    ne = math.ceil(np.mean(eleNE)*100)/100
    se = math.ceil(np.mean(eleSE)*100)/100
    nw = math.ceil(np.mean(eleNW)*100)/100
    sw = math.ceil(np.mean(eleSW)*100)/100
    
    return[n,s,e,w,nw,sw,ne,se]



try:
    db = MySQLdb.connect('challenger.cww0gaxyuygc.us-west-2.rds.amazonaws.com', 'h3amza', 'password1', 'challenge')
    cursor = db.cursor()
    cursor2 = db.cursor()
    cursor.execute("""SELECT id,latitude,longitude from elevation;""")
    for row in cursor.fetchall():
        id = int(row[0])
        lat = float(row[1])
        lng = float(row[2])
        #print lat
        #print lng
        d = directionalElevation(lat,lng,101)
        #print d
        cursor2.execute("""UPDATE elevation SET elevationN = %f,elevationS = %f, elevationE = %f, elevationW = %f, elevationNW = %f, elevationSW = %f, elevationNE = %f, elevationSE = %f WHERE id =%d"""%(d[0],d[1],d[2],d[3],d[4],d[5],d[6],d[7],id))
        db.commit()
        
        

    cursor.close()
    cursor2.close()
    
except MySQLdb.Error, e:
  
    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)




