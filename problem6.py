#!/usr/bin/env python3
from DataStructures import LinkedList  # <-- implementation here


def main():
    print(u"\nTesting LinkedList unions and intersections \u2699")

    # Test case 1
    print(u"\u0009\u22C5 Testing normal linked lists")

    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    intersection_a = [6, 4, 6, 21]
    union_a = [6, 32, 4, 9, 6, 1, 11, 21, 1, 3, 2, 4, 35, 65, 3]
    intersection = linked_list_1.intersect(linked_list_2)
    union = linked_list_1.union(linked_list_2)

    assert(intersection == intersection_a)
    print(u"\t\t\u22C5 Normal list intersection test passed \U0001F44D")
    assert(union == union_a)
    print(u"\t\t\u22C5 Normal lists union test passed \U0001F44D")

    # Test case 2
    print(u"\t\u22C5 Testing empty list")
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    element_2 = []

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    intersection_a = []
    union_a = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    intersection = linked_list_3.intersect(linked_list_4)
    union = linked_list_3.union(linked_list_4)

    assert(intersection == intersection_a)
    print(u"\t\t\u22C5 Empty list intersection passed \U0001F44D")
    assert(union == union_a)
    print(u"\t\t\u22C5 Empty list union test passed \U0001F44D")

    print(u"\u0009\u22C5 empty list test passed \U0001F44D")


if __name__ == '__main__':
    main()
    print(u"All tests passed! \U0001F60E")
