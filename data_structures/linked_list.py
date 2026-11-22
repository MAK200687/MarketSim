
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = newNode

    def display(self):
        if self.head is None:
            print("Trade history is empty")
            return

        current = self.head

        while current is not None:
            current.data.displaytradeinfo()
            print("--------------------")
            current = current.next

    def search(self, tradeID):
        current = self.head

        while current is not None:
            if current.data.ID == tradeID:
                return current.data

            current = current.next

        return None
