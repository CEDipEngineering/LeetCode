class Stack:
    def __init__(self):
        # Your subclass must not access this attribute
        self._items = []

    def push(self, value):
        self._items.append(value)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[-1]

    def empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self._items)


class StackWithMin(Stack):
    # Create whatever methods you need
    def __init__(self):
        super().__init__()
        self._min_stack = Stack()

    def push(self, value):
        if len(self._min_stack) == 0:
            self._min_stack.push(value)
        elif value <= self._min_stack.peek():
            self._min_stack.push(value)
        super().push(value)

    def pop(self):
        if super().peek() == self._min_stack.peek():
            self._min_stack.pop()
        return super().pop()

    def minimum(self):
        return self._min_stack.peek()
    

if __name__ == "__main__":
    s = StackWithMin()
    s.push(10)
    s.push(5)
    s.push(3)
    s.push(7)
    print(s.pop())
    print(s.minimum())
    print(s.pop())
    print(s.minimum())