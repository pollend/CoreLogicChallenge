from app.maps import google_maps

def test():
	return google_maps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
