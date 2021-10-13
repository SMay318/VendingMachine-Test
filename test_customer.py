import unittest
from customer import Customer

class TestGetWalletCoin(unittest.TestCase):
    """Tests for Customer's get_wallet_coin method"""
    def setUp(self):
        self.customer = Customer()
    def test_can_return_quarter(self):
        """Pass in 'Quarter', method should return a Quarter instance"""
        returned_coin = self.customer.get_wallet_coin('Quarter')
        self.assertEqual(returned_coin.value, .25)
    def test_can_return_dime(self):
        """Pass in 'Quarter', method should return a Quarter instance"""
        returned_coin = self.customer.get_wallet_coin('Dime')
        self.assertEqual(returned_coin.value, .10)
    def test_can_return_nickel(self):
        """Pass in 'Quarter', method should return a Quarter instance"""
        returned_coin = self.customer.get_wallet_coin('Nickel')
        self.assertEqual(returned_coin.value, .05)
    def test_can_return_penny(self):
        """Pass in 'Quarter', method should return a Quarter instance"""
        returned_coin = self.customer.get_wallet_coin('Penny')
        self.assertEqual(returned_coin.value, .01)
    def test_invalid_coins(self):
        """Pass in invalid str, method should return a Failed Test"""
        invalid_value = None
        # message = "This is an invalid choice."
        returned_coin = self.customer.get_wallet_coin('"asdf"')
        self.assertIsNone(returned_coin, invalid_value)

if __name__ == '__main__':
    unittest.main()
    