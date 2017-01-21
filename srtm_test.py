import srtm
geo_elevation_data = srtm.get_data()
print(geo_elevation_data.get_elevation( 39.7391536,-104.9847034))
image = geo_elevation_data.get_image((500, 500), (37.811330,37.761062), (-122.367505, -122.510783), 600)
# the image s a standard PIL object, you can save or show it:
image.show()