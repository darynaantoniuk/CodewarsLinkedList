"""Can you get the loop?"""


class Node:
    """class Node"""
    def __init__(self, data=None):
        """init method"""
        self.data = data
        self.next = None


def loop_size(node):
    """loop_size function"""
    slow = node
    fast = node
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return 0

    count = 1
    current = slow.next
    while current != slow:
        count += 1
        current = current.next

    return count
