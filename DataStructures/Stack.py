class Stack:
    class Node:
        def __init__(self, data):
            self.data = data
            self.__next = None

        @property
        def next(self):
            return self.__next

        @next.setter
        def next(self, next):
            if isinstance(next, Stack.Node):
                self.__next = next

    # end Stack.Node
    def __init__(self):
        self.__size = 0
        self.__head = None

    def __inc(self):
        self.__size += 1

    def __dec(self):
        self.__size -= 1

    @property
    def size(self):
        return self.__size

    @property
    def is_empty(self):
        return not self.size

    # added the ability to add a whole list at once, adding a prefix to each.
    # simplifies the directory search
    def push(self, val, prefix=""):
        if isinstance(val, list):
            for i in val:
                self.push(prefix + i)
            return
        head = self.Node(val)
        head.next = self.__head
        self.__head = head
        self.__inc()

    def pop(self):
        t = self.__head.data
        self.__head = self.__head.next
        self.__dec()
        return t

    def peek(self):
        if self.__head is None:
            return None
        return self.__head.data
