import unittest
from customer import Customer
from wallet import Wallet

class TestFillWallet(unittest.TestCase):
    """Test to see if the wallet object has a length of 88"""
    def setUp(self):
        self.customer = Customer()
    """Instantiate wallet object and test money list has len of 88"""
    def test_fill_wallet(self):
        self.wallet = Wallet()
        test_var = self.customer.wallet.money
        self.assertEqual(len(test_var), 88)

if __name__ == '__main__':
    unittest.main()


   