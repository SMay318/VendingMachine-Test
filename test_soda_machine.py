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

class TestRegisterHasCoin(unittest.TestCase):
    """Test that each type of coin will return True"""
    def setUp(self) -> None:
        self.soda_machine = SodaMachine()
    def test_register_has_coin_penny(self):
        """Test that penny will return True"""
        returned_penny = self.soda_machine.register_has_coin("Penny")
        self.assertTrue(returned_penny)
    def test_register_has_coin_nickel(self):
        """Test that nickel will return True"""
        returned_nickel = self.soda_machine.register_has_coin("Nickel")
        self.assertTrue(returned_nickel)
    def test_register_has_coin_dime(self):
        """Test that dime will return True"""
        returned_dime = self.soda_machine.register_has_coin("Dime")
        self.assertTrue(returned_dime)
    def test_register_has_coin_quarter(self):
        """Test that quarter will return True"""
        returned_quarter = self.soda_machine.register_has_coin("Quarter")
        self.assertTrue(returned_quarter)
    def test_not_valid_coin_name(self):
        """Test that a non-valid coin name will return false"""
        not_valid_coin_name = self.soda_machine.register_has_coin("daasdd")
        self.assertFalse(not_valid_coin_name)

class TestDetermineChangeValue(unittest.TestCase):
    def setUp(self):
        self.soda_machine = SodaMachine()
    def test_total_payment_higher(self):
        """Testing with the total payment being higher"""
        total_payment_higher = self.soda_machine.determine_change_value(.75, .6)
        self.assertEqual(total_payment_higher, .15)
    def test_select_soda_price_higher(self):
        """Testing when select_soda_price is higher"""
        soda_price_higher = self.soda_machine.determine_change_value(.5,.6)
        self.assertNotEqual(soda_price_higher, .1)
    def test_with_two_equal_values(self):
        equal_value = self.soda_machine.determine_change_value(.6,.6)
        self.assertEqual(equal_value, 0)

class TestCalculateCoinValue(unittest.TestCase):
    def setUp(self):
        self.soda_machine = SodaMachine()
    def test_calculate_coin_value(self):
        self.list_of_coins = []
        quarter = Quarter()
        dime = Dime()
        nickel = Nickel()
        penny = Penny()
        self.list_of_coins.append(quarter)
        self.list_of_coins.append(dime)
        self.list_of_coins.append(nickel)
        self.list_of_coins.append(penny)
        coins = self.soda_machine.calculate_coin_value(self.list_of_coins)
        self.assertEqual(coins, .41)
        
   
       

if __name__ == '__main__':
    unittest.main()

