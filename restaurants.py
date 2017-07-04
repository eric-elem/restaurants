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
                    "&radius=500&type=restaurant&key="+maps_api_key)
            connection.request("GET",uri)
            response=connection.getresponse()
            if(response.status==200):
                results=response.read()
                return json.loads(results)
            else:
                return 'Reponse not successful. Try again.'
            restaurants={}
            return restaurants
        else:
            return 'Undefined'
    else:
        return 'Undefined'

def main():
    lat=raw_input('\nEnter latitude: ')
    lon=raw_input('Enter longitude: ')
    print '\nGetting restaurants...\n'
    restaurants=get_restaurants(lat,lon)
    if isinstance(restaurants,dict):
        for restaurant in restaurants['results']:
            print restaurant['name']
    else:
        print restaurants
    print '\n'  

if __name__ == '__main__':
    main()