# i have used the helper code provided by udacity in completing this code

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    if user in group.get_users():
        return True
    else:
        list = group.get_groups()
        for character in list:
            return is_user_in_group(user, character)
    return False


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)


# Test Cases

# Edge case 1
print(is_user_in_group(user='', group=parent))
# Expected output
# [False]
# Edge case 2
print(is_user_in_group(user='', group=child))
# Expected output
# False

# Test 1
print(is_user_in_group(user='child_user', group=parent))
#  Expected output
#  [False]

#  Test 2
print(is_user_in_group(user='parent_user', group=parent))
# Expected output
# [False]
#  Test 3
print(is_user_in_group(user='sub_child_user', group=parent))
# Expected output
# True
