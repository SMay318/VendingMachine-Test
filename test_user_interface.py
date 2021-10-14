import unittest
import user_interface
from cans import Cola
from cans import OrangeSoda
from cans import RootBeer
from coins import Penny
from coins import Nickel
from coins import Dime
from coins import Quarter

class TestValidateMainMenue(unittest.TestCase):
    """Pass in each number 1-4, ensure the tuple of (True, number) is returned
    Pass in a different number, ensure (False, None) is returned"""
    def test_validate_main_menu_one(self):
       one = user_interface.validate_main_menu(1)
       self.assertTrue(one)
    def test_validate_main_menu_two(self):
       two = user_interface.validate_main_menu(2)
       self.assertTrue(two)
    def test_validate_main_menu_three(self):
       three = user_interface.validate_main_menu(3)
       self.assertTrue(three)
    def test_validate_main_menu_four(self):
       four = user_interface.validate_main_menu(4)
       self.assertTrue(four)
    def test_validate_main_menu_false(self):
       seven = user_interface.validate_main_menu(7)
       self.assertTrue(seven)

class TestTryParseInt(unittest.TestCase):

      def test_try_parse_int_ten(self):
         """Pass in 10 and ensure int value 10 is returned"""
         ten = user_interface.try_parse_int(10)
         self.assertEqual(ten, 10)
      def test_try_parse_int_hello(self):
         """Pass in hello and ensure 0 is returned"""
         hello = user_interface.try_parse_int("hello")
         self.assertEqual(hello, 0)

class TestGetUniqueCanNames(unittest.TestCase):
   """a. Instantiate 6 cans (two of each type) and append them to a list. Pass the list into this
function, ensure the returned list only contains 3 names
b. Pass in an empty list. Ensure an empty list is returned."""
   def test_get_unique_can_names(self):
      self.can_list = []
      cola_one = Cola()
      cola_two = Cola()
      orange_soda_one = OrangeSoda()
      orange_soda_two = OrangeSoda()
      root_beer_one = RootBeer()
      root_beer_two = RootBeer()
      self.can_list.append(cola_one)
      self.can_list.append(cola_two)
      self.can_list.append(orange_soda_one)
      self.can_list.append(orange_soda_two)
      self.can_list.append(root_beer_one)
      self.can_list.append(root_beer_two)
      cans = user_interface.get_unique_can_names(self.can_list)
      self.assertEqual(len(cans),3)
   def test_get_empty_can_list(self):
      self.empty_can_list = []
      cans = user_interface.get_unique_can_names(self.empty_can_list)
      self.assertEqual(len(cans), 0)
class DisplayPaymentValue(unittest.TestCase):
   def test_returned_payment_value(self):
      """instantiate 4 coin types and append them to a list and ensure returned value is .41"""
      self.list_of_coins = []
      quarter = Quarter()
      dime = Dime()
      nickel = Nickel()
      penny = Penny()
      self.list_of_coins.append(quarter)
      self.list_of_coins.append(dime)
      self.list_of_coins.append(nickel)
      self.list_of_coins.append(penny)
      coins = user_interface.display_payment_value(self.list_of_coins)
      self.assertEqual(coins, .41)
   def test_empty_list_equals_zero(self):
      """Pass in an empty list and ensure returned value is 0"""
      self.empty_coins_list = []
      coins = user_interface.display_payment_value(self.empty_coins_list)
      self.assertEqual(coins, 0)


if __name__ == '__main__':
    unittest.main()


