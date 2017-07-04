import numbers
def get_restaurants(lat,lon):
    if isinstance(lat,numbers.Number) and isinstance(lon,numbers.Number):
        if lat>-85 and lat<85 and lon>-180 and lon<180:
            restaurants={}
            return restaurants
        else:
            return 'Undefined'
    else:
        return 'Undefined'