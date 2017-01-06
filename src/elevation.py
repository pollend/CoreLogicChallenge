import googlemaps,json
gmaps = googlemaps.Client(key='AIzaSyBkFhUMEuDdlSBXYp18Pmy7bMKwK0M7IrM')

# passed address
geocode_result = gmaps.geocode('814 Lantana Ave Brea, CA')

#lng/lat
lat = geocode_result[0]['geometry']['location']['lat']
lng = geocode_result[0]['geometry']['location']['lng']
print(lat)
print(lng)
elevation_result = gmaps.elevation((lat,lng))
print(elevation_result[0]['elevation'])
