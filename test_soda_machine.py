import unittest
from soda_machine import SodaMachine

class TestFill_Register(unittest.TestCase):
    """
    Instantiate a SodaMachine object, test that its register list has a len of 88
    """
    def setUp(self):
        self.soda_machine = SodaMachine()
    
    def test_fill_register(self):
        test_var = self.soda_machine.register
        self.assertEqual(len(test_var),88)
   
    """Testing to see if invetory list has a length of 30"""
    def test_fill_inventory(self):
        test_var = self.soda_machine.inventory
        self.assertEqual(len(test_var), 30)

if __name__ == '__main__':
    unittest.main()

