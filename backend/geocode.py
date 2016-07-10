import requests

location_cache = {}

def geocode(tweet):
    user = tweet.get('user')
    if user is None:
        user = {}
    location = user.get('location')
    if location is None:
        location = ''

    if location in location_cache:
        return location_cache[location]

    url = 'http://nominatim.openstreetmap.org/search?q=%s&format=json&limit=1' % location
    result = requests.get(url).json()
    if result:
        location_cache[location] = {'lon': result[0].get('lon'), 'lat': result[0].get('lat')}
        return location_cache[location]
    return None
