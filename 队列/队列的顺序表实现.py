class QueueUnderFlowError(ValueError):
    pass


class Queue:
    def __init__(self, init_len=8):
        self._elems = [0] * init_len
        self._head = 0
        self._num = 0
        self._len = init_len

    def is_empty(self):
        return self._num == 0

    def enqueue(self, elem):
        if self._num == self._len:
            self.__extend()
        first_empty = (self._head + self._num) % self._len
        self._elems[first_empty] = elem
        self._num += 1

    def dequeue(self):
        if self.is_empty():
            raise QueueUnderFlowError
        elem = self._elems[self._head]
        self._head = (self._head + 1)%self._len
        self._num -= 1
        return elem

    def __extend(self):
        old_len = self._len
        self._len *= 2
        new_elems = [0] * self._len
        for i in range(old_len):
            new_elems[i] = self._elems[(self._head + i) % old_len]
        self._elems = new_elems
        self._head = 0
        self._rear = self._num - 1


if __name__ == "__main__":
    q = Queue()
    q.enqueue(0)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(7)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    q.enqueue(8)
    q.enqueue(9)
    q.enqueue(10)
    q.enqueue(11)
    q.enqueue(12)
    q.enqueue(13)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
