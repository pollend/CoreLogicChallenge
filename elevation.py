
from app.database import db
from app.google_maps import google_maps
# need to add column ALTER TABLE `AKZA-6UK256_ChapmanData_12072016` ADD ALTITUDE FLOAT NULL;

rows = db.query("SELECT ID,`PARCEL LEVEL LATITUDE`,`PARCEL LEVEL LONGITUDE` FROM `AKZA-6UK256_ChapmanData_12072016` WHERE ALTITUDE IS NULL");
for row in rows:
    print id
    id = row["ID"]
    lat = row["PARCEL LEVEL LATITUDE"]
    lng = row["PARCEL LEVEL LONGITUDE"]
    elevation_result = google_maps.elevation((lat, lng))
    db.query('''UPDATE `AKZA-6UK256_ChapmanData_12072016` SET ALTITUDE = :elevation WHERE ID = :id''',id = id, elevation = elevation_result[0]['elevation'])