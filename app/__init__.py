import records
import googlemaps
from app import config

google_maps = googlemaps.Client(key=config.GOOGLE_API)
db = records.Database(config.DATABASE)
