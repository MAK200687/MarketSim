from abc import ABC, abstractmethod
import csv
import json

class InvalidTransactionError(Exception):
    pass

class Transaction(ABC):
    def __init__(self, city, date, time, amount, status):
        self.city = city
        self.date = date
        self.time = time
        self.amount = amount
        self.status = status

    @property
    def city(self):
        return self._city
    @city.setter
    def city(self, value):
        if not value or not str(value).strip():
            raise InvalidTransactionError(" cannot be empty")
        self._city = str(value).strip()

    @property
    def date(self):
        return self._date
    @date.setter
    def date(self, value):
        if not value or not str(value).strip():
            raise InvalidTransactionError("cannot be empty")
        self._date = str(value).strip()

    @property
    def time(self):
        return self._time
    @time.setter
    def time(self, value):
        if not value or not str(value).strip():
            raise InvalidTransactionError(" cannot be empty")
        self._time = str(value).strip()

    @property
    def amount(self):
        return self._amount
    @amount.setter
    def amount(self, value):
        value = float(value)         
        if value <= 0:
            raise InvalidTransactionError("amount must be greater than 0")
        self._amount = value

    @property
    def status(self):
        return self._status
    @status.setter
    def status(self, value):
        if not value or not str(value).strip():
            raise InvalidTransactionError(" cannot be empty")
        self._status = str(value).strip()

    ###abs method 
    @abstractmethod
    def get_net_impact(self) -> float:
        pass

class CreditTransaction(Transaction):
    def __init__(self, city, date, time, amount, status):
        super().__init__(city, date, time, amount, status)
    def get_net_impact(self):
        return self.amount

class DebitTransaction(Transaction):
    def __init__(self, city, date, time, amount, status):
        super().__init__(city, date, time, amount, status)

    def get_net_impact(self) -> float:
        return -self.amount



#####part b 

class FileLoader(ABC):
    @abstractmethod
    def parse_file(self, filepath: str) -> list[Transaction]:
        pass

class JSONLoader(FileLoader):

    def parse_file(self, filepath: str) -> list[Transaction]:

        items = []
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return items

        if not isinstance(data, list):
            return items

        for row in data:
            try:
                kind = str(row["Type"]).strip()
                if kind == "Credit":
                    obj = CreditTransaction(row["City"], row["Date"], row["Time"], row["Amount"], row["Status"])
                elif kind == "Debit":
                    obj = DebitTransaction(row["City"], row["Date"], row["Time"], row["Amount"], row["Status"])
                else:
                    raise InvalidTransactionError("type's unknown")
                items.append(obj)

            except (KeyError, ValueError, TypeError, InvalidTransactionError):
                continue

        return items


class CSVLoader(FileLoader):
    def parse_file(self, filepath: str) -> list[Transaction]:
        items = []
        try:
            with open(filepath, "r", newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)

                for row in reader:
                    try:
                        kind = str(row["Type"]).strip()

                        if kind == "Credit":
                            obj = CreditTransaction(row["City"], row["Date"], row["Time"], row["Amount"], row["Status"])

                        elif kind == "Debit":
                            obj = DebitTransaction(row["City"], row["Date"], row["Time"], row["Amount"], row["Status"])

                        else:
                            raise InvalidTransactionError("type's unknown")

                        items.append(obj)

                    except (KeyError, ValueError, TypeError, InvalidTransactionError):
                        continue

        except FileNotFoundError:
            return items

        return items

    


