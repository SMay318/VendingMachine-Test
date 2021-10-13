import coins


class Wallet:
    def __init__(self):
        self.money = []
        self.fill_wallet()

    def fill_wallet(self):
        """Adds coins to money list"""
        for index in range(8):
            self.money.append(coins.Quarter())
        for index in range(10):
            self.money.append(coins.Dime())
        for index in range(20):
            self.money.append(coins.Nickel())
        for index in range(50):
            self.money.append(coins.Penny())
