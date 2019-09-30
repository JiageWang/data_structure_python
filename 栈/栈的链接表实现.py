class StackUnderFlowError(ValueError):
    pass


class Node:
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class Stack:
    def __init__(self):
        self._top = None

    def is_empty(self):
        return self._top is None

    def push(self, elem):
        node = Node(elem)
        node.next = self._top
        self._top = node

    def pop(self):
        if self.is_empty():
            raise StackUnderFlowError
        elem = self._top.elem
        self._top = self._top.next
        return elem

    def top(self):
        if self.is_empty():
            raise StackUnderFlowError
        return self._top.elem


if __name__ == "__main__":
    s = Stack()
    s.push(0)
    s.push(1)
    s.push(2)
    print(s.pop())
    print(s.pop())
    print(s.pop())
