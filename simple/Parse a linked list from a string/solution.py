"""Parse a linked list from a string"""


class Node:
    """class node"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def linked_list_from_string(s: str):
    """linked list from a string"""
    if s == "None":
        return None
    node_lst = s.split(" -> ")
    new_node = None
    for i in list(reversed(node_lst[:-1])):
        head = Node(int(i), new_node)
        new_node = head
    return head
