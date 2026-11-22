
from classes.stock import Stock
from classes.investor import Investor
from classes.portfolio import Portfolio
from classes.exchange import Exchange
from classes.order import Order


investor = Investor("Ammar", 1)
portfolio = Portfolio()
exchange = Exchange()

stock1 = Stock("ABC", "ABC Company", 100)
stock2 = Stock("XYZ", "XYZ Company", 200)

stocks = {
    "ABC": stock1,
    "XYZ": stock2
}


print("\nTEST 1: EMPTY QUEUE")
print(exchange.pendingOrders.is_empty())


print("\nTEST 2: ADD PENDING ORDERS")

order1 = Order(1, "ABC", "BUY", 10, 100)
order2 = Order(2, "ABC", "SELL", 5, 100)

exchange.addPendingOrder(order1)
exchange.addPendingOrder(order2)

exchange.displayPendingOrders()


print("\nTEST 3: PROCESS FIRST ORDER")

exchange.processNextOrder(investor, portfolio, stocks)

order1.displayOrder()
investor.display()
portfolio.displayholdings()


print("\nTEST 4: PROCESS SECOND ORDER")

exchange.processNextOrder(investor, portfolio, stocks)

order2.displayOrder()
investor.display()
portfolio.displayholdings()


print("\nTEST 5: CHECK FIFO")

print("First order status:", order1.status)
print("Second order status:", order2.status)


print("\nTEST 6: CHECK EMPTY QUEUE")

print(exchange.pendingOrders.is_empty())


print("\nTEST 7: PROCESS EMPTY QUEUE")

exchange.processNextOrder(investor, portfolio, stocks)


print("\nTEST 8: INSUFFICIENT SHARES")

order3 = Order(3, "XYZ", "SELL", 5, 200)

exchange.addPendingOrder(order3)
exchange.processNextOrder(investor, portfolio, stocks)

print("Order status:", order3.status)


print("\nTEST 9: INVALID STOCK")

order4 = Order(4, "DEF", "BUY", 2, 100)

exchange.addPendingOrder(order4)
exchange.processNextOrder(investor, portfolio, stocks)

print("Order status:", order4.status)


print("\nTEST 10: FINAL TRADE HISTORY")

exchange.trades.display()


print("\nALL QUEUE INTEGRATION TESTS COMPLETED")
