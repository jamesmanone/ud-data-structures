#!/usr/bin/env python3
from .PriorityQueue import MinPriorityQueue
from .LRU_Cache import LRU_Cache as Cache


class HuffmanTree:
    class Node:
        def __init__(self, char=None):
            self.char = char
            self.priority = 0
            self.left = None
            self.right = None

        @property
        def is_leaf(self):
            return self.left is None and self.right is None

        def trim(self):
            if self.left is not None:
                self.left.trim()
            if self.right is not None:
                self.right.trim()
            del self.priority

        def inc_priority(self):
            if self.priority is not None:
                self.priority += 1

        @classmethod
        def from_nodes(cls, left, right):
            node = cls()
            node.left = left
            node.right = right
            node.priority = left.priority + right.priority
            return node

    def __init__(self, string):
        map = {}
        if len(string) == 0:
            self.__root = HuffmanTree.Node()
            return
        for char in string:
            if char not in map:
                map[char] = HuffmanTree.Node(char=char)
            map[char].inc_priority()

        q = MinPriorityQueue()
        for char in map:
            q.enq(map[char], map[char].priority)

        while q.size > 1:
            node = HuffmanTree.Node.from_nodes(q.deq(), q.deq())
            q.enq(node, node.priority)

        self.__root = q.deq()
        self.__root.trim()
        self.__cache = Cache(20)

    # recursive tree walking to get char code
    def __get_bits(self, char, node):
        if node is None or node.is_leaf:
            return None
        if node.left is not None and node.left.char == char:
            return '0'
        if node.right is not None and node.right.char == char:
            return '1'
        left = self.__get_bits(char, node.left)
        right = self.__get_bits(char, node.right)
        if left is None and right is None:
            return None
        if left is not None:
            return '0' + left
        if right is not None:
            return '1' + right

    # Check the cache first, __get_bits on cache miss
    def __read_through_cache(self, char):
        code = self.__cache.get(char)
        if code != -1:
            return code
        return self.__cache.set(char, self.__get_bits(char, self.__root))

    def encode(self, string):
        out_str = ''
        for char in string:
            out_str += self.__read_through_cache(char)
        return out_str

    def decode(self, eString):
        out_str = ''
        node = self.__root
        for bit in eString:
            if bit == '0':
                node = node.left
            else:
                node = node.right
            if node.is_leaf:
                out_str += node.char
                node = self.__root
        return out_str
