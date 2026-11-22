
from classes.stock import Stock
from classes.portfolio import Portfolio
from classes.trade import Trade
from classes.order import Order
from data_structures.linked_list import LinkedList
from data_structures.stack import Stack
from data_structures.queue import Queue
from datetime import datetime
from classes.database import Database


class Exchange:
    def __init__(self):
        self.trades = LinkedList()
        self.undoStack = Stack()
        self.pendingOrders = Queue()
        self.database = Database()
        self.database.createTable()
        self.tradeCount = self.database.getLastTradeID()

    def buy(self, investor, portfolio, stock, quantity):
        if quantity <= 0:
            return False

        total = stock.price * quantity

        if investor.subtract(total) == False:
            print("Insufficient balance")
            return False

        portfolio.addshares(stock, quantity)

        now = datetime.now()

        self.tradeCount += 1

        newTrade = Trade(
            self.tradeCount,
            stock.symbol,
            "BUY",
            quantity,
            stock.price,
            now.strftime("%d-%m-%Y"),
            now.strftime("%H:%M")
        )

        self.trades.append(newTrade)
        self.database.saveTrade(newTrade)

        undoData = {
            "type": "BUY",
            "stock": stock,
            "quantity": quantity,
            "total": total,
            "trade": newTrade
        }

        self.undoStack.push(undoData)

        print("Purchase successful")
        return True

    def sell(self, investor, portfolio, stock, quantity):
        if quantity <= 0:
            return False

        if portfolio.removeshares(stock, quantity) == False:
            print("Insufficient shares")
            return False

        total = stock.price * quantity

        investor.add(total)

        now = datetime.now()

        self.tradeCount += 1

        newTrade = Trade(
            self.tradeCount,
            stock.symbol,
            "SELL",
            quantity,
            stock.price,
            now.strftime("%d-%m-%Y"),
            now.strftime("%H:%M")
        )

        self.trades.append(newTrade)
        self.database.saveTrade(newTrade)

        undoData = {
            "type": "SELL",
            "stock": stock,
            "quantity": quantity,
            "total": total,
            "trade": newTrade
        }

        self.undoStack.push(undoData)

        print("Sale successful")
        return True

    def undoLastTransaction(self, investor, portfolio):
        if self.undoStack.is_empty():
            print("No transaction available to undo")
            return False

        undoData = self.undoStack.peek()

        stock = undoData["stock"]
        quantity = undoData["quantity"]
        total = undoData["total"]
        trade = undoData["trade"]

        if undoData["type"] == "BUY":

            holding = portfolio.holdings.get(stock.symbol)

            if holding is None or holding[1] < quantity:
                print("Cannot undo purchase")
                return False

            portfolio.removeshares(stock, quantity)
            investor.add(total)

        elif undoData["type"] == "SELL":

            if investor.subtract(total) == False:
                print("Insufficient balance to undo sale")
                return False

            portfolio.addshares(stock, quantity)

        self.undoStack.pop()

        trade.reversed = True
        self.database.markReversed(trade.ID)

        print("Transaction successfully undone")
        return True

    def executeOrder(self, order, investor, portfolio, stock):
        if order.type == "BUY":
            result = self.buy(investor, portfolio, stock, order.quantity)

        elif order.type == "SELL":
            result = self.sell(investor, portfolio, stock, order.quantity)

        else:
            order.updateStatus("Rejected")
            print("Invalid order type")
            return False

        if result:
            order.updateStatus("Completed")
        else:
            order.updateStatus("Rejected")

        return result

    def addPendingOrder(self, order):
        self.pendingOrders.enqueue(order)
        print("Order added to pending queue")

    def processNextOrder(self, investor, portfolio, stocks):
        if self.pendingOrders.is_empty():
            print("No pending orders")
            return False

        order = self.pendingOrders.dequeue()

        stock = stocks.get(order.symbol)

        if stock is None:
            order.updateStatus("Rejected")
            print("Stock not found")
            return False

        return self.executeOrder(order, investor, portfolio, stock)

    def displayPendingOrders(self):
        if self.pendingOrders.is_empty():
            print("No pending orders")
            return

        for order in self.pendingOrders.items:
            order.displayOrder()
            print("--------------------")
