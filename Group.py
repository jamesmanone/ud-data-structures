from DataStructures import Set


class Group:
    def __init__(self, name):
        self.name = name
        self.groups = list()
        self.users = Set()

    def __eq__(self, group):
        if isinstance(group, Group):
            return self.name == group.name
        elif type(group) == str:
            return group == self.name
        else:
            return False

    def __str__(self):
        return "Group: " + self.name

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.insert(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name
