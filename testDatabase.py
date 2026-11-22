
from classes.database import Database

db = Database()
db.createTable()

trades = db.getTrades()

print("SAVED TRADES:")
for trade in trades:
    print(trade)

db.close()
