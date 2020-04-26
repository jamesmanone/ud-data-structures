#!/usr/bin/env python3
from problem1 import main as LRU
from problem2 import main as file_recursion
from problem3 import main as huffman
from problem4 import main as active_directory
from problem5 import main as blockchain
from problem6 import main as union


if __name__ == "__main__":
    LRU()
    file_recursion()
    huffman()
    active_directory()
    blockchain()
    union()

    print(u"\nAll tests passed! \U0001F60E\n")
