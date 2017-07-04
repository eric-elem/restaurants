import unittest
from restaurants import get_restaurants
class TestRestaurants(unittest.TestCase):
    
    def test_isstring(self):
        self.assertEqual(get_restaurants('lat','long'), 
                            'Latitude and longitude must be numbers',msg='Input shoud not be a string')
    def test_islessthanminlat(self):
        self.assertEqual(get_restaurants(-100,32), 
                            'Latitude and/or longitude out of range',msg='Latitude shoud be > -85')
    def test_isgreaterthanmaxlat(self):
        self.assertEqual(get_restaurants(86,90.6788), 
                            'Latitude and/or longitude out of range',msg='Latitude shoud be < 85')
    def test_islessthanminlong(self):
        self.assertEqual(get_restaurants(-30.1,-196), 
                            'Latitude and/or longitude out of range',msg='Longitude shoud be > -180')
    def test_isgreaterthanmaxlong(self):
        self.assertEqual(get_restaurants(80,300.9), 
                            'Latitude and/or longitude out of range',msg='Latitude shoud be < 180')
    def test_isvalid(self):
        self.assertEqual(isinstance(get_restaurants(0.3688,32.1988),dict), 
                True,msg='dict object shoud be returned for valid input')

if __name__ == '__main__':
    unittest.main()