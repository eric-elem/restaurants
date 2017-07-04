import unittest
from restaurants import get_restaurants
class TestRestaurants(unittest.TestCase):
    
    def test_isstring(self):
        self.assertEqual(get_restaurants('lat','long'), 
                            'Undefined',msg='Input shoud not be a string')
    def test_islessthanminlat(self):
        self.assertEqual(get_restaurants(-100,32), 
                            'Undefined',msg='Latitude shoud be > -85')
    def test_isgreaterthanmaxlat(self):
        self.assertEqual(get_restaurants(86,90.6788), 
                            'Undefined',msg='Latitude shoud be < 85')
    def test_islessthanminlong(self):
        self.assertEqual(get_restaurants(-30.1,-196), 
                            'Undefined',msg='Longitude shoud be > -180')
    def test_isgreaterthanmaxlong(self):
        self.assertEqual(get_restaurants(80,300.9), 
                            'Undefined',msg='Latitude shoud be < 180')
    def test_isvalid(self):
        self.assertEqual(isinstance(get_restaurants(0.3688,32.1988),dict), 
                True,msg='dict object shoud be returned for valid input')

if __name__ == '__main__':
    unittest.main()