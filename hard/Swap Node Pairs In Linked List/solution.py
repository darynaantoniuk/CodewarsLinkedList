"""Swap Node Pairs In Linked List"""


class Node:
    """class Node"""
    def __init__(self, data=None):
        """init method"""
        self.data = data
        self.next = None


def swap_pairs(head):
    """swap_pairs function"""
    if head is None or head.next is None:
        return head

    new_head = head.next
    prev = None
    current = head

    while current and current.next:
        first = current
        second = current.next
        next_pair = second.next

        second.next = first
        first.next = next_pair

        if prev:
            prev.next = second

        prev = first
        current = next_pair

    return new_head
