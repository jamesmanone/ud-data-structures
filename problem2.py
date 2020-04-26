#!/usr/bin/env python3
import os
from DataStructures import Stack


def find_files(ext, path):
    to_visit = Stack()
    results = []
    to_visit.push(os.listdir(path), path + '/')
    while not to_visit.is_empty:
        next = to_visit.pop()
        if os.path.isfile(next) and next.endswith(ext):
            results.append(next)
        elif os.path.isdir(next):
            to_visit.push(os.listdir(next), next + '/')
    return results


def main():
    answer = ['./testdir/subdir1/a.c', './testdir/subdir5/a.c',
              './testdir/t1.c', './testdir/subdir3/subsubdir1/b.c']
    print(u"\nTesting recursive filetype search \u2699")
    candidate = find_files('c', './testdir')
    for item in answer:
        assert(item in candidate)
    print(u"\u0009\u22C5 File recursion search test passed \U0001F44D")


if __name__ == "__main__":
    main()
    print(u"All tests passed! \U0001F60E")
