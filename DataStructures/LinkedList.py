

class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.__head = None
        self.__size = 0
        self.__last = None

    def __repr__(self):
        if self.size == 0:
            return '[]'
        out = '['
        for item in self:
            out += f"{item}, "
        return out[:-2] + ']'

    def __contains__(self, data):
        head = self.__head
        while head is not None:
            if head.data == data:
                return True
        return False

    def __len__(self):
        return self.size

    @property
    def size(self):
        return self.__size

    @property
    def is_empty(self):
        return self.size == 0

    def __getitem__(self, i):
        if i > self.size - 1:
            raise IndexError("linkedlist index out of range")
        head = self.__head
        j = 0
        while j < i:
            head = head.next
            j += 1
        return head.data

    def __setitem__(self, i, data):
        if i > self.size:
            raise IndexError('index out of range')
        if i == self.size:  # allow append with self[len(self)] = x
            self.append(data)

        head = self.__head
        for _ in range(i):
            head = head.next
        head.data = data

    def __iter__(self):
        head = self.__head
        while head is not None:
            yield head.data
            head = head.next

    def __eq__(self, b):
        if not (isinstance(b, LinkedList) or isinstance(b, list)):
            return False
        tstb = self.from_iterable(b)
        tst = self.copy()

        for item in tst:
            if not tstb.remove(item):
                return False
        if tstb.is_empty:
            return True
        return False

    @property
    def last(self):
        if self.__last is not None:
            return self.__last.data
        return None

    def __inc_size(self):
        self.__size += 1

    def __dec_size(self):
        if self.size > 0:
            self.__size -= 1

    def copy(self):
        out = LinkedList()
        for item in self:
            out.append(item)
        return out

    def remove(self, data):
        head = self.__head
        if head.data == data:
            self.__head = head.next
            self.__dec_size()
            return True
        while head.next is not None and head.next.data != data:
            head = head.next
        if head.next is None:
            return False
        self.__dec_size()
        head.next = head.next.next
        if head.next is None:
            self.__tail = head
        return True

    def append(self, data):
        if self.__last is not None:
            self.__last.next = LinkedList.Node(data)
            self.__last = self.__last.next
            self.__inc_size()

        elif self.__head is None:
            self.__head = LinkedList.Node(data)
            self.__last = self.__head
            self.__inc_size()

        else:  # fixing an invalid state
            head = self.__head
            i = 1
            while head.next is not None:
                head = head.next
                i += 1
            head.next = LinkedList.Node(data)
            self.__last = head.next
            self.__size = i + 1

    def pop(self, data):
        head = self.__head
        if head.data == data:
            self.__head = head.next
        else:
            while head.next is not None and head.next.data != data:
                head = head.next
            if head.next is None:
                return
            head.next = head.next.next
        self.__dec_size()

    def union(self, b):
        if not isinstance(b, LinkedList):
            return
        map = {}

        out = LinkedList()
        for item in b:
            if item not in map:
                map[item] = 1
            else:
                map[item] += 1
            out.append(item)

        for item in self:
            if item in map and map[item] > 0:
                map[item] -= 1
            else:
                out.append(item)
        return out

    def intersect(self, b):
        map = {}
        for item in b:
            if item not in map:
                map[item] = 1
            else:
                map[item] += 1
        out = LinkedList()
        for item in self:
            if item in map and map[item] > 0:
                out.append(item)
                map[item] -= 1
        return out

    @classmethod
    def from_iterable(cls, iterable):
        out = cls()
        for item in iterable:
            out.append(item)
        return out
