import unittest
from soda_machine import SodaMachine
from coins import Penny
from coins import Nickel
from coins import Dime
from coins import Quarter

class TestFillRegister(unittest.TestCase):
    """Instantiate a SodaMachine object, test that its register list has a len of 88"""
    def setUp(self):
        self.soda_machine = SodaMachine()
    
    def test_fill_register(self):
        test_var = self.soda_machine.register
        self.assertEqual(len(test_var),88)
   
class TestFillInventory(unittest.TestCase):
    """Testing to see if invetory list has a length of 30"""
    def setUp(self):
        self.soda_machine = SodaMachine()
    def test_fill_inventory(self):
        test_var = self.soda_machine.inventory
        self.assertEqual(len(test_var), 30)

class TestGetCoinFromRegister(unittest.TestCase):
    """Test each type of coin can be returned from register"""
    def setUp(self):
        self.soda_machine = SodaMachine()

    def test_get_coin_from_register(self):
        returned_penny = self.soda_machine.get_coin_from_register("Penny")
        self.assertTrue(returned_penny)

if __name__ == '__main__':
    unittest.main()

