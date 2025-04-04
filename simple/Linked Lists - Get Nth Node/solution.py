"""Get Nth Node"""

class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def get_nth(node, index):
    """get_nth function"""
    if node is None:
        raise IndexError("Emplty linked list.")
    if index < 0:
        raise IndexError("Index out of range.")
    count = 0
    while node is not None:
        if count == index:
            return node
        count += 1
        node = node.next
    if count <= index:
        raise IndexError("Index out of range.")
    return node
