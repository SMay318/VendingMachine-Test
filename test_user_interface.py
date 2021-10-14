import unittest
import user_interface

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

if __name__ == '__main__':
    unittest.main()


