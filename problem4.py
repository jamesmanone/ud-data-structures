#!/usr/bin/env python3
# print(u"\u0009\u22C5")
from Group import Group
from DataStructures import Stack
from DataStructures import Set


def is_user_in_group(user, group):
    to_explore = Stack()
    groups = Set()
    to_explore.push(group)

    while not to_explore.is_empty:
        next = to_explore.pop()
        groups.insert(next)
        for g in next.get_groups():
            if g not in groups:
                to_explore.push(g)

    for group in groups:
        if user in group.get_users():
            return True
    return False


def main():
    print(u"\nTesting Active Directory \u2699")
    admin = Group("admin")
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    child.add_group(sub_child)
    parent.add_group(child)
    child.add_group(admin)

    user = 'limited'
    sudo = 'admin'

    sub_child.add_user(user)
    admin.add_user(sudo)

    assert(is_user_in_group(user, sub_child))
    print(u"\u0009\u22C5 User lookup passed \U0001F44D")

    assert(is_user_in_group(user, parent))
    print(u"\u0009\u22C5 Recursive lookup passed \U0001F44D")

    assert(not is_user_in_group(user, admin))
    print(u"\u0009\u22C5 Limited privilege test passed \U0001F44D")

    assert(is_user_in_group(sudo, admin))
    print(u"\u0009\u22C5 Admin privilege test passed \U0001F44D")


if __name__ == "__main__":
    main()
    print(u"All tests passed! \U0001F60E")
