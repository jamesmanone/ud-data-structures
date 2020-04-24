from collections import deque


class LRU_Cache:
    # Nodes are imutable / copy on write / copy on read
    class Node:
        def __init__(self, key, value):
            self.__key = key
            self.__value = value
            self.__next = None
            self.__valid = True

        @property
        def value(self):
            if self.is_valid:
                return self.__value
            return None

        @property
        def key(self):
            if self.is_valid:
                return self.__key
            return None

        @property
        def is_valid(self):
            return self.__valid

        @property
        def next(self):
            if self.is_valid:
                return self.__next
            return None

        @next.setter
        def next(self, next):
            if self.is_valid and isinstance(next, LRU_Cache.Node):
                self.__next = next
            else:
                self.__next = None

        def invalidate(self):
            next = self.__next
            self.__valid = False
            del self.__key
            del self.__value
            del self.__next
            return next

        def update(self, value):
            new_node = LRU_Cache.Node(self.key, value)
            new_node.next = self.invalidate()
            return new_node

        @classmethod
        def from_Node(cls, node):
            new_node = cls(node.key, node.value)
            new_node.next = node.invalidate()
            return new_node

    # end LRU_Cache.Node
    def __init__(self, cap):
        self.__cache = [None] * int(cap*1.43)  # target ~0.7 utl
        self.__q = deque()
        self.__size = 0
        self.__cap = cap

    def __inc_size(self):
        self.__size += 1
        return self.__size

    def __dec_size(self):
        self.__size -= 1
        return self.__size

    def __get_hash(self, key):
        length = len(key) - 1
        hash = 0
        for char in key:
            hash += ord(char) * (31**length)
            length -= 1
        return hash % len(self.__cache)

    @property
    def __full(self):
        return self.__size >= self.__cap

    def __deleteLRU(self):
        node = self.__q.pop()
        while not node.is_valid:
            node = self.__q.pop()

        key = node.key
        hash = self.__get_hash(key)
        head = self.__cache[hash]

        if head.key == key:
            self.__cache[hash] = head.invalidate()
            self.__dec_size()

        elif head.next is not None:
            while head.next is not None and head.next.key != key:
                head = head.next
            head.next = head.next.invalidate()
            self.__dec_size()

    def __put(self, key, val):
        if self.__full:
            self.__deleteLRU()
        hash = self.__get_hash(key)
        node = LRU_Cache.Node(key, val)
        node.next = self.__cache[hash]
        self.__cache[hash] = node
        self.__inc_size()
        self.__q.appendleft(node)
        return val

    def get(self, key):
        if type(key) != str:
            key = str(key)
        hash = self.__get_hash(key)
        head = self.__cache[hash]
        if head is None:
            return -1

        elif head is not None and head.key == key:
            head = LRU_Cache.Node.from_Node(head)
            self.__cache[hash] = head

        elif head.next is None:
            return -1

        else:
            while head.next is not None and head.next.key != key:
                head = head.next
            if head.next is None:
                return -1
            head.next = LRU_Cache.Node.from_Node(head.next)
            head = head.next

        val = head.value
        self.__q.appendleft(head)
        return val

    def set(self, key, val):
        if type(key) != str:
            key = str(key)
        hash = self.__get_hash(key)
        head = self.__cache[hash]
        if head is None:
            return self.__put(key, val)
        if head is not None and head.key == key:
            head = head.update(val)
            self.__cache[hash] = head
            self.__q.appendleft(head)
            return val

        elif head is not None:
            while head.next is not None and head.next.key != key:
                head = head.next
            if head.next is None:
                return self.__put(key, val)

            head.next = head.next.update(val)
            self.__q.appendleft(head.next)
            return val
