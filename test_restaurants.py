import unittest
from restaurants import get_restaurants
class TestRestaurants(unittest.TestCase):
    
    def test_isstring(self):
        self.assertEqual(get_restaurants('my','loc'), 
                            'Undefined',msg='Input shoud be a string')
    
if __name__ == '__main__':
    unittest.main()