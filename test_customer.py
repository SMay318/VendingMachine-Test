import unittest
from coins import Dime, Nickel, Quarter
from customer import Customer
from wallet import Wallet

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
        returned_coin = self.customer.get_wallet_coin('"asdf"')
        self.assertIsNone(returned_coin)

# if __name__ == '__main__':
#     unittest.main()

class TestAddCoinsToWallet(unittest.TestCase):
    """Tests for Customer's add_coins_to_wallet method"""
    def setUp(self):
        self.customer = Customer()
       
    def test_length_of_customers_money_list(self):
        quarter = Quarter()
        nickel = Nickel()
        dime = Dime()
        self.customer.add_coins_to_wallet([quarter,nickel,dime])
        self.assertEqual(len(self.customer.wallet.money), 91)
    
    def test_pass_in_empty_money_list(self):
        self.customer.add_coins_to_wallet([])
        self.assertEqual(len(self.customer.wallet.money), 88)

if __name__ == '__main__':
    unittest.main()