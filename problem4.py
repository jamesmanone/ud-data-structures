#!/usr/bin/env python3
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


if __name__ == "__main__":
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")
    admin = Group("admin")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)
    child.add_group(admin)

    uinsubchild = is_user_in_group(sub_child_user, sub_child)
    uinchild = is_user_in_group(sub_child_user, child)
    uinparent = is_user_in_group(sub_child_user, parent)
    uinadmin = is_user_in_group(sub_child_user, admin)

    print('user in subchild: {}'.format(uinsubchild))
    print('user in child: {}'.format(uinchild))
    print("user in parent: {}".format(uinparent))
    print('user in admin: {}'.format(uinadmin))
