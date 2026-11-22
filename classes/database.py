
import sqlite3
import os

class Database:
    def __init__(self):
        self.dbPath = os.path.join("data", "marketsim.db")

        self.connection = sqlite3.connect(self.dbPath)
        self.cursor = self.connection.cursor()

    
    def createTable(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS trades (
                ID INTEGER PRIMARY KEY,
                symbol TEXT,
                type TEXT,
                quantity INTEGER,
                EXEprice REAL,
                date TEXT,
                time TEXT,
                Tvalue REAL,
                reversed INTEGER DEFAULT 0
            )
        """)

        self.connection.commit()

    
    def saveTrade(self, trade):
        self.cursor.execute("""
            INSERT INTO trades (ID, symbol, type, quantity, EXEprice, date, time, Tvalue)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            trade.ID,
            trade.symbol,
            trade.type,
            trade.quantity,
            trade.EXEprice,
            trade.date,
            trade.time,
            trade.Tvalue
        ))

        self.connection.commit()

    
    def getTrades(self):
        self.cursor.execute("SELECT * FROM trades")
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()

    
    def getLastTradeID(self):
        self.cursor.execute("SELECT MAX(ID) FROM trades")
        result = self.cursor.fetchone()
        
        if result[0] is None:
            return 0

        return result[0]

    def markReversed(self, tradeID):
        self.cursor.execute(
            "UPDATE trades SET reversed = 1 WHERE ID = ?",
            (tradeID,)
        )
        self.connection.commit()

    




