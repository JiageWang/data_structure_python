class Node:
    def __init__(self, elem):
        self.elem = elem
        self.next = None
        self.pre = None


class CircleDoubleLinkList:
    def __init__(self):
        self._head = None
        self._rear = None

    def is_empty(self):
        return self._head is None

    def length(self):
        if self.is_empty():
            return 0
        cur = self._head
        count = 1
        while cur != self._rear:
            cur = cur.next
            count += 1
        return count

    def travel(self):
        if self.is_empty():
            return
        cur = self._head
        print('[', end='')
        while cur.next is not self._head:
            print(cur.elem, end=' ')
            cur = cur.next
        print(cur.elem, end=']\n')

    def append(self, elem):
        node = Node(elem)
        if self._head is None:
            self._head = node
            node.next = node
            node.pre = node
        else:
            self._rear.next = node
            self._head.pre = node
            node.pre = self._rear
            node.next = self._head
        self._rear = node

    def add(self, elem):
        node = Node(elem)
        if self.is_empty():
            self._rear = node
            node.next = node
            node.pre = node
        else:
            self._rear.next = node
            self._head.pre = node
            node.pre = self._rear
            node.next = self._head
        self._head = node

    def insert(self, pos, elem):
        if pos > self.length() - 1:
            self.append(elem)
        elif pos <= 0:
            self.add(elem)
        else:
            node = Node(elem)
            count = 0
            cur = self._head
            while count<pos:
                cur = cur.next
                count += 1
            node.next = cur
            node.pre = cur.pre
            cur.pre.next = node
            cur.pre = node

    def remove(self, elem):
        if self.is_empty():
            return
        cur = self._head
        while cur.next != self._head:
            if cur.elem == elem:
                if cur==self._head:
                    self._rear.next = self._head.next
                    self._head.next.pre = self._rear
                    self._head = self._head.next
                else:
                    cur.next.pre = cur.pre
                    cur.pre.next = cur.next
                break
            else:
                cur = cur.next
        if cur==self._rear and cur.elem==elem:
            self._head.pre = self._rear.pre
            self._rear.pre.next = self._head
            self._rear = self._rear.pre

    def reverse(self):
        """双链表反转"""
        if self.is_empty():
            return
        head = self._head
        rear = self._rear
        while head.next!=rear:
            rear.elem, head.elem = head.elem, rear.elem
            head = head.next
            rear = rear.pre
            if head==rear:
                break
        else:
            rear.elem, head.elem = head.elem, rear.elem







if __name__ == "__main__":
    cdll = CircleDoubleLinkList()
    print(cdll.length())
    print(cdll.is_empty())
    cdll.travel()

    cdll.append(5)
    cdll.insert(0, 0)
    cdll.add(6)
    cdll.insert(3, 1)
    cdll.insert(1, 2)
    cdll.insert(2, 3)
    print(cdll.length())
    print(cdll.is_empty())
    cdll.travel()
    cdll.remove(6)
    cdll.remove(1)
    # cdll.remove(0)
    # cdll.remove(3)
    # cdll.remove(2)
    print(cdll.length())
    print(cdll.is_empty())
    cdll.travel()
    cdll.reverse()
    cdll.travel()
