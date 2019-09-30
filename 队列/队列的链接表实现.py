class QueueUnderFlowError(ValueError):
    pass


class Node:
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class Queue:
    def __init__(self):
        self._head = None
        self._rear = None

    def is_empty(self):
        return self._head is None

    def enqueue(self, elem):
        node = Node(elem)
        if self.is_empty():
            self._head = node
            self._rear = node
        else:
            self._rear.next = node
            self._rear = node

    def dequeue(self):
        if self.is_empty():
            raise QueueUnderFlowError
        else:
            elem = self._head.elem
            self._head = self._head.next
        return elem

    def peek(self):
        if self.is_empty():
            raise QueueUnderFlowError
        else:
            elem = self._head.elem
        return elem


if __name__ == "__main__":
    q = Queue()
    q.enqueue(0)
    q.enqueue(1)
    q.enqueue(2)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
