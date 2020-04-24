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


if __name__ == "__main__":
    print(find_files('c', './testdir'))
