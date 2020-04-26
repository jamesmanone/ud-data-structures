

class LRU_Cache:
    # Nodes are imutable / copy on write / copy on read
    class Node:
        def __init__(self, key, value):
            self.__key = key
            self.__value = value
            self.__next = None
            self.__valid = True
            self.__qnext = None
            self.__qprev = None
            self.__q = None

        def __repr__(self):
            prev = f"{self.qprev.key if self.qprev is not None else 'None'}"
            next = f"{self.qnext.key if self.qnext is not None else 'None'}"
            return f"{prev}<--\u007b{self.key}: {self.value}\u007D-->{next}"

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
            if isinstance(next, LRU_Cache.Node) and self.qnext != next:
                self.__next = next
            else:
                self.__next = None

        @property
        def qnext(self):
            return self.__qnext

        @qnext.setter
        def qnext(self, next):
            if isinstance(next, LRU_Cache.Node) and self.__qnext != next:
                self.__qnext = next
                next.__qprev = self
            elif self.__qnext == next:
                return
            else:
                self.__qnext = None

        @property
        def qprev(self):
            return self.__qprev

        @qprev.setter
        def qprev(self, prev):
            if isinstance(prev, LRU_Cache.Node) and self.qprev != prev:
                self.__qprev = prev
                prev.qnext = self
            elif self.qprev == prev:
                return
            else:
                self.__qprev = None

        def setQ(self, q):
            self.__q = q

        def unqueue(self):
            if self.qnext is None or self.qprev is None:
                self.__q.notify(self)
            else:
                self.qprev.qnext = self.qnext
                self.qnext.qprev = self.qprev
                self.__q.notify(self)
            self.qnext = None
            self.qprev = None

        def invalidate(self):
            '''
            Invalidate sets Node.__valid to false and removes itself from the
            deletion queue by stiching qnext and qprev together. Also notifies
            the queue to handle the case where self is __head or __tail of the
            queue
            '''
            self.__valid = False
            if self.__q is not None:
                self.__q.notify(self)
            if self.qnext is not None and self.qprev is not None:
                self.qprev.qnext = self.qnext
            return self.__next

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
    # Like a doubly linked list, but with only append and pop(left). The Nodes
    # can delete themselves from the queue in the event of a set or get
    class Deletion_Queue:
        def __init__(self):
            self.__head = None
            self.__tail = None
            self.__size = 0

        def __repr__(self):
            out = "head\n"
            head = self.__head
            while head is not None:
                out += repr(head)
                out += '\n'
                head = head.qnext
            out += "tail"
            return out

        @property
        def size(self):
            return self.__size

        @property
        def is_empty(self):
            return self.__size == 0

        def __inc_size(self):
            self.__size += 1

        def __dec_size(self):
            if self.__size > 0:
                self.__size -= 1

        def __len__(self):
            return self.size

        def notify(self, node):
            self.__dec_size()
            if node == self.__head:
                self.__head = self.__head.qnext
                if self.__head is not None:
                    self.__head.qprev = None
                node.qprev = None
                node.qnext = None
            if node == self.__tail:
                self.__tail = node.qprev
                if self.__tail is not None:
                    self.__tail.qnext = None
                node.qprev = None
                node.qnext = None

        def append(self, node):
            self.__inc_size()
            node.setQ(self)
            if self.__head is None:
                self.__head = node
                self.__tail = node
            else:
                self.__tail.qnext = node  # setting this stiches them together
                self.__tail = node

        def pop(self):
            if self.is_empty:
                return
            self.__dec_size()
            node = self.__head
            self.__head = node.qnext
            if self.__head is not None:
                self.__head.qprev = None
            else:
                self.__tail = None
                self.__size = 0
            return node

    # end LRU_Cache.Deletion_Queue
    def __init__(self, cap):
        if cap < 1:
            raise ValueError("minimum cache size is 1")
        self.__cache = [None] * int(cap*1.43)  # target ~0.7 utl
        self.__q = LRU_Cache.Deletion_Queue()
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
        self.__q.append(node)
        return val

    def get(self, key):
        if type(key) != str:
            key = str(key)
        hash = self.__get_hash(key)
        head = self.__cache[hash]

        while head is not None and head.key != key:
            head = head.next
        if head is None:
            return -1

        head.unqueue()
        val = head.value
        self.__q.append(head)
        return val

    def set(self, key, val):
        if type(key) != str:
            key = str(key)
        hash = self.__get_hash(key)
        head = self.__cache[hash]

        while head is not None and head.key != key:
            head = head.next
        if head is not None:
            head.value = val
            head.unqueue()
            self.__q.append(head)
            return val
        return self.__put(key, val)
