"""Linked Lists - Alternating Split"""


class Node:
    """class Node"""
    def __init__(self, data=None):
        """init method"""
        self.data = data
        self.next = None

class Context:
    """class Context"""
    def __init__(self, first, second):
        """init method"""
        self.first = first
        self.second = second

def alternating_split(head):
    """alternating_split function"""
    if head is None or head.next is None:
        raise ValueError

    first_head = head
    second_head = head.next
    first_tail = first_head
    second_tail = second_head

    current = head.next.next
    is_first = True

    while current:
        if is_first:
            first_tail.next = current
            first_tail = first_tail.next
        else:
            second_tail.next = current
            second_tail = second_tail.next
        is_first = not is_first
        current = current.next

    first_tail.next = None
    second_tail.next = None
    return Context(first_head, second_head)
