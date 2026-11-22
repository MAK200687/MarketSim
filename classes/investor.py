
class Investor:
    def __init__(self, name, id):
        self.name = name
        self._id = id
        self.__balance = 100000

    def display(self):
        print("Investor name:", self.name)
        print("Investor ID:", self._id)
        print("Investor balance:", self.__balance)

    def add(self, amount):
        self.__balance += amount
        return self.__balance

    def subtract(self, amount):
        if amount > self.__balance:
            return False
        else:
            self.__balance -= amount
            return self.__balance

    def getBalance(self):
        return self.__balance

    def setBalance(self, amount):
        self.__balance = amount
