
#from app.database import db
#from app.google_maps import google_maps
# need to add column ALTER TABLE `AKZA-6UK256_ChapmanData_12072016` ADD ALTITUDE FLOAT NULL;
##
##rows = db.query("SELECT ID,`PARCEL LEVEL LATITUDE`,`PARCEL LEVEL LONGITUDE` FROM `AKZA-6UK256_ChapmanData_12072016` WHERE ALTITUDE IS NULL");
##for row in rows:
##    print id
##    id = row["ID"]
##    lat = row["PARCEL LEVEL LATITUDE"]
##    lng = row["PARCEL LEVEL LONGITUDE"]
##    elevation_result = google_maps.elevation((lat, lng))
##    db.query('''UPDATE `AKZA-6UK256_ChapmanData_12072016` SET ALTITUDE = :elevation WHERE ID = :id''',id = id, elevation = elevation_result[0]['elevation'])

import MySQLdb
import sys
import srtm

elevation_data = srtm.get_data()
try:
    db = MySQLdb.connect('challenger.cww0gaxyuygc.us-west-2.rds.amazonaws.com', 'h3amza', 'password1', 'challenge')
    cursor = db.cursor()
    cursor2 = db.cursor()
    cursor.execute("""SELECT id,longitude,latitude from elevation;""")
    for row in cursor.fetchall():
        id = int(row[0])
        lat = float(row[1])
        lng = float(row[2])
        ele = float(elevation_data.get_elevation(lng,lat))
        print elevation_data.get_elevation(lng,lat)
        cursor2.execute("""UPDATE elevation SET elevation=%f WHERE id =%d"""%(ele,id))
        db.commit()
        
        

    cursor.close()
    cursor2.close()
    
except MySQLdb.Error, e:
  
    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)
