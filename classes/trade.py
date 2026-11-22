
class Trade:
    def __init__(self, ID, symbol, type, quantity, EXEprice, date, time):
        self.ID = ID
        self.symbol = symbol
        self.type = type
        self.quantity = quantity
        self.EXEprice = EXEprice
        self.date = date
        self.time = time
        self.Tvalue = quantity * EXEprice

    def displaytradeinfo(self):
        print("Trade ID:", self.ID)
        print("Stock Symbol:", self.symbol)
        print("Trade Type:", self.type)
        print("Quantity:", self.quantity)
        print("Execution Price:", self.EXEprice)
        print("Date:", self.date)
        print("Time:", self.time)
        print("Trade Value:", self.Tvalue)

