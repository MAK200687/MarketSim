
import json
import os


class JsonStorage:
    def __init__(self):
        self.filePath = "data/investor.json"

    def saveAccount(self, investor, portfolio):
        account = {
            "name": investor.name,
            "id": investor._id,
            "balance": investor.getBalance(),
            "holdings": {}
        }

        for symbol in portfolio.holdings:
            quantity = portfolio.holdings[symbol][1]
            account["holdings"][symbol] = quantity

        with open(self.filePath, "w") as file:
            json.dump(account, file, indent=4)

    def loadAccount(self, investor, portfolio, stocks):
        if not os.path.exists(self.filePath):
            return

        with open(self.filePath, "r") as file:
            account = json.load(file)

        investor.setBalance(account["balance"])

        for symbol in account["holdings"]:
            if symbol in stocks:
                quantity = account["holdings"][symbol]
                portfolio.addshares(stocks[symbol], quantity)
