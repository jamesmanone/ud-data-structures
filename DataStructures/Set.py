
class Set:
    class Node:
        def __init__(self, key):
            self.__key = key
            self.next = None

        @property
        def key(self):
            return self.__key

        def __eq__(self, key):
            return self.key == key

    def __init__(self, capacity=20):
        self.__size = 0
        self.__data = [None] * int(capacity*1.43)  # target ~0.7 utl
        self.__cap = int(0.7 * len(self.__data))

    def __iter__(self):
        for bucket in self.__data:
            head = bucket
            while head is not None:
                yield head.key
                head = head.next

    def __contains__(self, key):
        return self.search(key)

    def __inc_size(self):
        self.__size += 1
        return self.__size

    def __dec_size(self):
        if self.__size > 0:
            self.__size -= 1
        return self.__size

    @property
    def size(self):
        return self.__size

    def __enlarge(self):
        data = self.__data
        self.__data = [None] * int((self.__cap * 4) * 1.43)  # Quaduple cap
        self.__cap = int(0.7 * len(self.__data))
        self.__size = 0
        for datum in data:
            head = datum
            while head is not None:
                self.insert(head.key)
                head = head.next

    def __get_hash(self, key):
        if type(key) != str:
            key = str(key)
        length = len(key) - 1
        hash = 0
        for char in key:
            hash += ord(char) * (31**length)
            length -= 1
        return hash % len(self.__data)

    def insert(self, key):
        if self.search(key):  # no duplicates
            return
        if self.size >= self.__cap:
            self.__enlarge()
        self.__inc_size()
        node = Set.Node(key)
        hash = self.__get_hash(key)
        node.next = self.__data[hash]
        self.__data[hash] = node

    def search(self, key):
        hash = self.__get_hash(key)
        head = self.__data[hash]
        while head is not None and head.key != key:
            head = head.next
        if head is not None:
            return True

    def delete(self, key):
        hash = self.__get_hash(key)
        head = self.__data[hash]

        if head is None:
            return

        if head.key == key:
            self.__dec_size()
            self.__data[hash] = head.next
            return

        while head.next is not None and head.next.key != key:
            head == head.next
        if head.next is None:
            return
        head.next = head.next.next
        self.__dec_size()
        return

    def empty(self):
        for i in range(len(self.__data)):
            while self.__data[i] is not None:
                yield self.__data[i].key
                self.__data[i] = self.__data[i].next
