"""Remove Duplicates"""

class Node:
    """class Node"""
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    """remove_duplicates function"""
    if not head:
        return None

    current = head
    while current and current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next

    return head
