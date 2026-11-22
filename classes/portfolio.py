
from classes.stock import Stock

class Portfolio:
    def __init__(self):
        self.holdings = {}

    def addshares(self, stock, quantity):  #here it checks if stock already exists and js adds in the crrent quantity
        if quantity <= 0:
            return False

        if stock.symbol in self.holdings:
            self.holdings[stock.symbol][1] += quantity
        else:
            self.holdings[stock.symbol] = [stock, quantity]

        return True

    def removeshares(self, stock, quantity):
        if quantity <= 0:
            return False

        if stock.symbol in self.holdings: #validation here to check if we can even subtract from stock
            if self.holdings[stock.symbol][1] >= quantity:
                self.holdings[stock.symbol][1] -= quantity

                if self.holdings[stock.symbol][1] == 0:
                    del self.holdings[stock.symbol]

                return True
            else:
                return False
        else:
            return False

    def calculateshares(self):  #ok so basically its (Value of A x Total shares of A) + (value of B + total sharres of B)
        total = 0

        for symbol in self.holdings:
            stock = self.holdings[symbol][0]
            quantity = self.holdings[symbol][1]

            total = total + (stock.price * quantity)

        return total

    def displayholdings(self):
        if len(self.holdings) == 0:
            print("Portfolio is empty")
            return

        for symbol in self.holdings:
            stock = self.holdings[symbol][0]
            quantity = self.holdings[symbol][1]
            value = stock.price * quantity

            print("Stock:", stock.name)
            print("Symbol:", stock.symbol)
            print("Price:", stock.price)
            print("Quantity:", quantity)
            print("Total value:", value)
            print("--------------------")
