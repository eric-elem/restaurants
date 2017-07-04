import numbers
import httplib
import json
def get_restaurants(lat,lon):
    if isinstance(lat,numbers.Number) and isinstance(lon,numbers.Number):
        if lat>-85 and lat<85 and lon>-180 and lon<180:
            connection = httplib.HTTPSConnection('maps.googleapis.com')
            location=str(lat)+","+str(lon)
            maps_api_key='AIzaSyAgjjNmY1XnfAbZjSpYgh3VlvdwgbWXSzw'
            uri=("/maps/api/place/nearbysearch/json?location="+location+
                    "&radius=1000&type=restaurant&key="+maps_api_key)
            try:
                connection.request("GET",uri)
                response=connection.getresponse()
                if(response.status==200):
                    results=response.read()
                    return json.loads(results)
                else:
                    return 'Reponse not successful. Try again.'
                restaurants={}
                return restaurants
            except Exception:
                return 'Communication failure. Please try again later.'
        else:
            return 'Latitude and/or longitude out of range'
    else:
        return 'Latitude and longitude must be numbers'

def main():
    lat=raw_input('\nEnter latitude: ')
    lon=raw_input('Enter longitude: ')
    print '\nGetting restaurants...\n'
    try:
        restaurants=get_restaurants(float(lat),float(lon))
    except ValueError:
        restaurants=get_restaurants(lat,lon)
    if isinstance(restaurants,dict):
        if len(restaurants['results'])>0:
            for restaurant in restaurants['results']:
                print restaurant['name']
        else:
            print "Couldn't find restaurants near provided location"
    else:
        print restaurants
    print '\n'  

if __name__ == '__main__':
    main()