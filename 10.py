class Stack:
    def init(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty."

    def is_empty(self):
        return len(self.items) == 0

    def iter(self):
        self.current = len(self.items) - 1
        return self

    def next(self):
        if self.current >= 0:
            item = self.items[self.current]
            self.current -= 1
            return item
        else:
            raise StopIteration()

# Example usage:
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

for item in stack:
    print(item)

print("Popped item:", stack.pop())

for item in stack:
    print(item)
