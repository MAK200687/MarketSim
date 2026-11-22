
class Stock:
    def __init__(self, symbol, name, price):
        self.name = name
        self.symbol = symbol
        self.price = price

    def updatePrice(self, newPrice):
        self.price = newPrice
        print("Updated price for stock", self.symbol, self.price)

    def displayInfo(self):
        print("Stock details")
        print("Stock name:", self.name)
        print("Stock price:", self.price)
        print("Stock symbol:", self.symbol)
