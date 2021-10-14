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
    """Testing to see if penny is returned from register"""
    def test_get_coin_penny_from_register(self):
        returned_penny = self.soda_machine.get_coin_from_register("Penny")
        self.assertTrue(returned_penny)
    """Testing to see if nickel is returned from register"""
    def test_get_coin_nickel_from_register(self):
        returned_nickel = self.soda_machine.get_coin_from_register("Nickel")
        self.assertTrue(returned_nickel)
    """Testing to see if dime is returned from register"""
    def test_get_coin_dime_from_register(self):
        returned_dime = self.soda_machine.get_coin_from_register("Dime")
        self.assertTrue(returned_dime)
    """Testing to see if quarter is returned from register"""
    def test_get_coin_quarter_from_register(self):
        returned_quarter = self.soda_machine.get_coin_from_register("Quarter")
        self.assertTrue(returned_quarter)
    """Testing to see that passing in a string that is not a valid coin name will return none"""
    def test_not_valid_string_from_register(self):
        invalid_string = self.soda_machine.get_coin_from_register("asdasdas")
        self.assertIsNone(invalid_string)

"""Test that each type of coin will return True"""
class TestRegisterHasCoin(unittest.TestCase):
    def setUp(self) -> None:
        self.soda_machine = SodaMachine()
    def test_register_has_coin(self):
        """Test that penny will return True"""
        returned_penny = self.soda_machine.register_has_coin("Penny")
        self.assertTrue(returned_penny)
    def test_register_has_coin(self):
        """Test that nickel will return True"""
        returned_nickel = self.soda_machine.register_has_coin("Nickel")
        self.assertTrue(returned_nickel)
    def test_register_has_coin(self):
        """Test that dime will return True"""
        returned_dime = self.soda_machine.register_has_coin("Dime")
        self.assertTrue(returned_dime)
    def test_register_has_coin(self):
        """Test that quarter will return True"""
        returned_quarter = self.soda_machine.register_has_coin("Quarter")
        self.assertTrue(returned_quarter)


if __name__ == '__main__':
    unittest.main()

