class StackUnderFlowError(ValueError):
    pass


class Stack:
    def __init__(self):
        self._elems = []

    def is_empty(self):
        return len(self._elems) == 0

    def push(self, elem):
        self._elems.append(elem)

    def pop(self):
        if self.is_empty():
            raise StackUnderFlowError
        return self._elems.pop()

    def top(self):
        if self.is_empty():
            raise StackUnderFlowError
        return self._elems[-1]


if __name__ == "__main__":
    s = Stack()
    s.push(0)
    s.push(1)
    s.push(2)
    print(s.pop())
    print(s.pop())
    print(s.pop())
