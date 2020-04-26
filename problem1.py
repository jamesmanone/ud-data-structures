#!/usr/bin/env python3
from DataStructures import LRU_Cache  # <--implementation here
import random
from string import ascii_letters as letters


def rand_string():
    return ''.join(random.choice(letters) for _ in range(15))


def main():
    print(u"\nTesting LRU_Cache \u2699")
    cache = LRU_Cache(5)

    assert(cache.get("a") == -1)  # cache miss

    cache.set("a", 1)
    cache.set("b", 2)
    cache.set("c", 3)
    cache.set("d", 4)
    cache.set("e", 5)

    assert(cache.get("a") == 1)  # Still there
    assert(cache.get("e") == 5)
    cache.set("f", 6)

    assert(cache.get("a") == 1)  # get kept it from getting removed
    assert(cache.get("b") == -1)  # cache miss

    print(u'\u0009\u22C5 Small cache tests passed \U0001F44D')

    cache = LRU_Cache(50)

    longer = [rand_string() for _ in range(65)]

    for i, string in enumerate(longer):
        cache.set(string, i)

    for i in range(10):
        assert(cache.get(longer[i]) == -1)

    for i in range(20, 65):
        assert(cache.get(longer[i]) == i)

    print(u"\u0009\u22C5 Large cache tests passed \U0001F44D")

    exception = 0
    try:
        cache = LRU_Cache(0)
    except ValueError:
        exception = True
    assert(exception)

    print(u"\u0009\u22C5 Zero length cache test passed \U0001F44D")


if __name__ == '__main__':
    main()
    print(u"All tests passed \U0001F60E")
