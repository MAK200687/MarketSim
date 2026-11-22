
import csv

from classes.stock import Stock
from classes.investor import Investor
from classes.portfolio import Portfolio
from classes.order import Order
from classes.exchange import Exchange
from classes.JsonStorage import JsonStorage


def loadStocks():
    stocks = {}
    latestPrices = {}

    stockNames = {
        "ABC": "ABC Company",
        "XYZ": "XYZ Company",
        "DEF": "DEF Company",
        "GHI": "GHI Company",
        "JKL": "JKL Company"
    }

    with open("data/marketsim_stocks.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            symbol = row["Symbol"]
            date = row["Date"]
            price = float(row["Close"])

            if symbol not in latestPrices or date > latestPrices[symbol][0]:
                latestPrices[symbol] = [date, price]

    for symbol in latestPrices:
        name = stockNames.get(symbol, symbol + " Company")
        price = latestPrices[symbol][1]

        stocks[symbol] = Stock(symbol, name, price)

    return stocks


def displayStocks(stocks):
    print("\nAVAILABLE STOCKS")
    print("--------------------")

    for symbol in stocks:
        stocks[symbol].displayInfo()
        print("--------------------")


def main():

    stocks = loadStocks()

    investor = Investor("Ammar", "I1001")
    portfolio = Portfolio()

    jsonStorage = JsonStorage()
    jsonStorage.loadAccount(investor, portfolio, stocks)
    jsonStorage.saveAccount(investor, portfolio)

    exchange = Exchange()

    orderCount = 0

    print("\n================================")
    print("       WELCOME TO MARKETSIM")
    print("  VIRTUAL STOCK TRADING SYSTEM")
    print("================================")

    while True:

        print("\nMAIN MENU")
        print("1. View Available Stocks")
        print("2. View Account Balance")
        print("3. View Portfolio")
        print("4. Buy Stocks")
        print("5. Sell Stocks")
        print("6. View Trade History")
        print("7. Undo Last Transaction")
        print("8. Place Pending Order")
        print("9. View Pending Orders")
        print("10. Process Next Pending Order")
        print("11. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            displayStocks(stocks)

        elif choice == "2":

            investor.display()

        elif choice == "3":

            portfolio.displayholdings()

            print("Total Portfolio Value:", portfolio.calculateshares())

        elif choice == "4":

            symbol = input("Enter stock symbol: ").upper()

            if symbol not in stocks:
                print("Stock not found")
                continue

            try:
                quantity = int(input("Enter quantity: "))
            except ValueError:
                print("Please enter a valid quantity")
                continue

            result = exchange.buy(investor, portfolio, stocks[symbol], quantity)

            if result:
                jsonStorage.saveAccount(investor, portfolio)

        elif choice == "5":

            symbol = input("Enter stock symbol: ").upper()

            if symbol not in stocks:
                print("Stock not found")
                continue

            try:
                quantity = int(input("Enter quantity: "))
            except ValueError:
                print("Please enter a valid quantity")
                continue

            result = exchange.sell(investor, portfolio, stocks[symbol], quantity)

            if result:
                jsonStorage.saveAccount(investor, portfolio)

        elif choice == "6":

            exchange.trades.display()

        elif choice == "7":

            result = exchange.undoLastTransaction(investor, portfolio)

            if result:
                jsonStorage.saveAccount(investor, portfolio)

        elif choice == "8":

            symbol = input("Enter stock symbol: ").upper()

            if symbol not in stocks:
                print("Stock not found")
                continue

            orderType = input("Enter BUY or SELL: ").upper()

            if orderType != "BUY" and orderType != "SELL":
                print("Invalid order type")
                continue

            try:
                quantity = int(input("Enter quantity: "))
            except ValueError:
                print("Please enter a valid quantity")
                continue

            if quantity <= 0:
                print("Quantity must be greater than zero")
                continue

            orderCount += 1

            newOrder = Order(
                orderCount,
                symbol,
                orderType,
                quantity,
                stocks[symbol].price
            )

            exchange.addPendingOrder(newOrder)

        elif choice == "9":

            exchange.displayPendingOrders()

        elif choice == "10":

            result = exchange.processNextOrder(investor, portfolio, stocks)

            if result:
                jsonStorage.saveAccount(investor, portfolio)

        elif choice == "11":

            jsonStorage.saveAccount(investor, portfolio)

            print("\nThank you for using MarketSim!")
            break

        else:

            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
