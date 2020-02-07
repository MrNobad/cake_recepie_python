import unittest
from CakeShop import CakeShop

class TestCakeShop(unittest.TestCase):
    def setUp(self):
        cakes = ['Brownie', 'Cream', 'Chocolate']
        self.cakeShop = CakeShop('Nobad Cakes', cakes)

    def test_cake_shop_has_name(self):
        self.assertEquals('Nobad Cakes', self.cakeShop.name)

    def test_cake_shop_has_cakes(self):
        self.assertEquals(3, len(self.cakeShop.cakes))

if __name__ == '__main__': 
    unittest.main()