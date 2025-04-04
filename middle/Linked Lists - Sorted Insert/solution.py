"""Sorted Insert"""


class Node:
    """Node class"""
    def __init__(self, data):
        self.data = data
        self.next = None


def sorted_insert(head, data):
    """sorted_insert function"""
    new_head = Node(data)

    if head is None:
        return new_head

    if data < head.data:
        new_head.next = head
        return new_head

    current = head
    while current.next is not None and current.next.data < data:
        current = current.next

    new_head.next = current.next
    current.next = new_head
    return head
