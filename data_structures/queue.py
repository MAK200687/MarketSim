
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        if self.is_empty():
            return None

        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            return None

        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return

        for item in self.items:
            print(item)
