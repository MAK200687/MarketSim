
class Order:
    def __init__(self, ID, symbol, type, quantity, price):
        self.ID = ID
        self.symbol = symbol
        self.type = type
        self.quantity = quantity
        self.price = price
        self.status = "Pending"

    def displayOrder(self):
        print("Order ID:", self.ID)
        print("Stock Symbol:", self.symbol)
        print("Order Type:", self.type)
        print("Quantity:", self.quantity)
        print("Price:", self.price)
        print("Status:", self.status)

    
    def updateStatus(self, newstatus):
        if newstatus == "Pending" or newstatus == "Completed" or newstatus == "Rejected":
            self.status = newstatus
        else:
            print("invalid status")


