class Node(object):
    """节点"""

    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleLinkList(object):
    def __init__(self, node=None):
        self._head = node

    def length(self):
        count = 0
        cur = self._head
        while cur:
            count += 1
            cur = cur.next
        return count

    def is_empty(self):
        return self._head == None

    def travel(self):
        cur = self._head
        while cur:
            print(cur.elem, end=" ")
            cur = cur.next
        print("\n")

    def add(self, item):
        # 头插O(1)
        node = Node(item)
        node.next = self._head
        self._head = node

    def append(self, item):
        # 尾插O(n)
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next:
                cur = cur.next
            cur.next = node

    def insert(self, pos, elem):
        # 位置插O(n)
        if pos <= 0:
            self.add(elem)
        elif pos > self.length() - 1:
            self.append(elem)
        else:
            node = Node(elem)
            count = 0
            pre = self._head
            while count < pos - 1:
                count += 1
                pre = pre.next
            # 循环推出后， pre指向pos-1
            node.next = pre.next
            pre.next = node

    def remove(self, elem):
        cur = self._head
        pre = None
        while cur:
            if cur.elem == elem:
                # 先判断子节点是否为头节点
                if cur == self._head:
                    self._head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, elem):
        # O(n)
        cur = self._head
        while cur:
            if cur.elem == elem:
                return True
            else:
                cur = cur.next
        return False

    def reverse(self):
        """单链表反转"""
        p = None
        cur = self._head
        while cur is not None:
            self._head = cur.next
            cur.next = p
            p = cur
            cur = self._head

        self._head = p




if __name__ == "__main__":
    ll = SingleLinkList()
    ll.append(1)
    ll.travel()
    # ll.append(2)
    # ll.append(4)
    # ll.add(8)
    # ll.insert(3, 5)
    # ll.remove(2)
    ll.reverse()
    ll.travel()
    print(ll.length())
    print(ll.is_empty())
