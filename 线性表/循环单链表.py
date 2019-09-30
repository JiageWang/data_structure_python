class Node(object):
	"""节点"""
	def __init__(self, elem):
		self.elem = elem
		self.next = None


class CircleSingleLinkList(object):
	def __init__(self, node=None):
		self._head = node
		if self._head:
			self._head.next = self._head

	def length(self):
		if self.is_empty():
			return 0
		cur = self._head
		count = 1
		while cur.next != self._head:
			count += 1
			cur = cur.next
		return count

	def is_empty(self):
		return self._head == None

	def travel(self):
		if self.is_empty():
			return
		cur = self._head
		while cur.next != self._head:
			print(cur.elem, end=" ")
			cur = cur.next
		print(cur.elem)

	def add(self, item):
		# O(1)
		node = Node(item)
		if self.is_empty():
			self._head = node
			self._head.next = self._head
		else:
			# 寻找尾结点
			rear = self._head
			while rear.next != self._head:
				rear = rear.next
			node.next = self._head
			self._head = node
			rear.next = self._head


	def append(self, item):
		# O(n)
		node = Node(item)
		if self.is_empty():
			self._head = node
			self._head.next = self._head
		else:
			cur = self._head
			while cur.next != self._head:
				cur = cur.next
			cur.next = node
			node.next = self._head



	def insert(self, pos, elem):
		# O(n)
		if pos <= 0:
			self.add(elem)
		elif pos > self.length()-1:
			self.append(elem)
		else:	
			node = Node(elem)
			count = 0
			pre = self._head
			while count < pos-1:
				count += 1
				pre = pre.next
			# 循环推出后， pre指向pos-1
			node.next = pre.next
			pre.next = node

	def remove(self, elem):
		if self.is_empty():
			return 
		cur = self._head
		pre = None
		while cur.next != self._head:
			# 节点数大于1
			if cur.elem == elem:
				if cur == self._head:
					# 删除头节点
					rear = self._head
					# 寻找尾结点
					while rear.next != self._head:
						rear = rear.next
					rear.next = cur.next
					self._head = cur.next
				else:
					pre.next = cur.next
				break
			else:
				pre = cur
				cur = cur.next
		if cur.elem == elem:
			if cur == self._head:
				#节点数等于1
				self._head = None
			else:
				pre.next = self._head

	def search(self, elem):
		# O(n)
		cur = self._head
		while cur.next != self._head:
			if cur.elem == elem:
				return True
			else:
				cur = cur.next
		if cur.next == elem:
			return True
		return False





if __name__ == "__main__":
	ll= CircleSingleLinkList()
	print(ll.is_empty())
	print(ll.length())
	ll.travel()
	ll.append(1)
	ll.travel()
	ll.append(2)
	ll.append(4)
	ll.add(8)
	ll.insert(3, 5)
	ll.travel()
	ll.remove(2)
	ll.travel()
