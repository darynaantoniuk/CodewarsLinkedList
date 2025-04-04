"""Recursive Reverse"""

class Node:
    """class Node"""
    def __init__(self, data=None):
        """init method"""
        self.data = data
        self.next = None

def reverse(head):
    """reverse function"""
    if head is None or head.next is None:
        return head

    new_head = reverse(head.next)

    head.next.next = head
    head.next = None

    return new_head
