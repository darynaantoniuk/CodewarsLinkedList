""" Push & BuildOneTwoThree"""


class Node:
    """class Node"""
    def __init__(self, data):
        self.data = data
        self.next = None


def push(head, data):
    """push function"""
    new_node = Node(data)
    new_node.next = head
    return new_node

def build_one_two_three():
    """build_one_two_three function"""
    head = None
    head = push(head, 3)
    head = push(head, 2)
    head = push(head, 1)
    return head
