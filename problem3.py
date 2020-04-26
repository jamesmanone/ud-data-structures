#!/usr/bin/env python3
from DataStructures import HuffmanTree  # <-- implementation here
# Also uses MinPriorityQueue from PriorityQueue.py
# Also uses LRU_Cache (through cache 'lookup' for decoding)
import sys


def huffman_encoding(string):
    tree = HuffmanTree(string)
    eString = tree.encode(string) if tree is not None else ''
    return (eString, tree)


def huffman_decoding(eString, tree):
    return tree.decode(eString)


def openfile(path):
    file = open(path)
    string = file.read()
    file.close()
    return string


def test_str(str):
    candidate, tree = huffman_encoding(str)
    assert(sys.getsizeof(str) > sys.getsizeof(int(candidate, base=2)))
    print(u"\u0009\u0009\u22C5 Size test passed  \U0001F44D")
    assert(str == huffman_decoding(candidate, tree))
    print(u"\u0009\u0009\u22C5 Accuracy test passed  \U0001F44D")


def main():
    print(u"\nTesting Huffman Tree \u2699")

    test1 = "The bird bird bird, the bird is the word"
    print(u"\u0009\u22C5 Testing normal string:")
    test_str(test1)
    test2 = openfile('tst.txt')
    print(u"\u0009\u22C5 Testing long string")
    test_str(test2)
    print(u"\u0009\u22C5 Testing empty string")
    candidate, tree = huffman_encoding('')
    assert(tree.decode(candidate) == '')
    print(u"\u0009\u0009\u22C5 Empty string test passed  \U0001F44D")


if __name__ == "__main__":
    main()
    print(u"All tests passed! \U0001F60E")
