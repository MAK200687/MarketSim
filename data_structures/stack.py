
class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if self.is_empty():
            return None

        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None

        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        if self.is_empty():
            print("Stack is empty")
            return

        for item in reversed(self.items):
            print(item)
