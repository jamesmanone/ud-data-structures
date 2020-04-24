#!/usr/bin/env python3
from HuffmanTree import HuffmanTree


def huffman_encoding(string):
    tree = HuffmanTree(string)
    return (tree.encode(string), tree)


def huffman_decoding(eString, tree):
    return tree.decode(eString)


def openfile(path):
    file = open(path)
    string = file.read()
    file.close()
    return string


if __name__ == "__main__":
    import sys
    a_great_sentence = "The bird bird bird, the bird is the word"

    print("would you like to read from a file? (press return to skip)")
    path = input(':>')
    if path:
        a_great_sentence = openfile(path)

    print("The size of the data is: {}\n".format(
            sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(
            int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
            sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
