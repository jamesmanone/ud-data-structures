#!/usr/bin/env python3


class MinPriorityQueue:
    class Node:
        def __init__(self, data, priority):
            self.data = data
            self.priority = priority
            self.next = None

    def __init__(self):
        self.__head = None
        self.__size = 0

    def __inc_size(self):
        self.__size += 1

    def __dec_size(self):
        if self.__size > 0:
            self.__size -= 1

    @property
    def is_empty(self):
        return self.__head is None

    @property
    def size(self):
        return self.__size

    def enq(self, data, priority):
        node = self.Node(data, priority)
        self.__inc_size()

        if self.is_empty:
            self.__head = node
            return

        head = self.__head
        if head.priority > priority:
            node.next = head
            self.__head = node
            return

        while head.next is not None and head.next.priority <= priority:
            head = head.next
        node.next = head.next
        head.next = node

    def deq(self):
        self.__dec_size()  # no effect is __size is 0
        if self.is_empty:
            return None
        data = self.__head.data
        self.__head = self.__head.next
        return data
