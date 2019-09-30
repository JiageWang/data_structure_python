class LNode:
    def __init__(self, elem):
        self.elem = elem
        self.pre = None
        self.next = None


class DoubleLinkList:
    def __init__(self):
        self._head = None
        self._rear = None

    def is_empty(self):
        return self._head is None

    def length(self):
        if self.is_empty():
            return 0
        count = 1
        cur = self._head
        while cur.next is not None:
            cur = cur.next
            count += 1
        return count

    def travel(self):
        cur = self._head
        while cur is not None:
            print(cur.elem, end=' ')
            cur = cur.next
        print('')

    def add(self, elem):
        """头插法 时间复杂度为O(1)"""
        node = LNode(elem)
        if not self.is_empty():
            self._head.pre = node  # 改变原首节点的前置节点
            node.next = self._head  # 改变新节点的后置节点
        self._head = node

    def append(self, elem):
        """尾插法 时间复杂度为O(1)"""
        node = LNode(elem)
        node.pre = self._rear
        if self.is_empty():
            self._head = node
        else:
            self._rear.next = node
        self._rear = node

    def insert(self, pos, elem):
        """位置插入 时间复杂度O(n)"""
        if pos <= 0:
            self.add(elem)
        elif pos > self.length() - 1:
            self.append(elem)
        else:
            node = LNode(elem)
            cur = self._head
            count = 0
            while count < pos - 1:
                cur = cur.next
                count += 1
            node.next = cur.next
            node.pre = cur
            cur.next.pre = node
            cur.next = node

    def remove(self, elem):
        cur = self._head
        while cur is not None:
            if cur.elem == elem:
                if cur == self._head:
                    self._head = cur.next
                    cur.next.pre = None
                elif cur == self._rear:
                    self._rear = cur.pre
                    cur.pre.next = None
                else:
                    cur.pre.next = cur.next
                    cur.next.pre = cur.pre
                break
            else:
                cur = cur.next

    def reverse(self):
        """双链表反转"""
        if self.is_empty():
            return
        head = self._head
        rear = self._rear
        while head.next != rear:
            rear.elem, head.elem = head.elem, rear.elem
            head = head.next
            rear = rear.pre
            if head == rear:
                break
        else:
            rear.elem, head.elem = head.elem, rear.elem



if __name__ == "__main__":
    dll = DoubleLinkList()
    print(dll.length())
    print(dll.is_empty())
    dll.travel()

    dll.append(2)
    dll.add(0)
    dll.add(1)
    dll.append(3)
    print(dll.length())
    print(dll.is_empty())
    dll.travel()

    dll.insert(4, 100)
    print(dll.length())
    print(dll.is_empty())
    dll.travel()
    print('=' * 30)

    dll.remove(1)
    print(dll.length())
    print(dll.is_empty())
    dll.travel()
    print('-----reversed-----')
    dll.reverse()
    dll.travel()
