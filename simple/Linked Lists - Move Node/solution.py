"""Move Node"""

class Node(object):
    """class Node"""
    def __init__(self, data):
        """init method"""
        self.data = data
        self.next = None


class Context(object):
    """class Context"""
    def __init__(self, source, dest):
        """init method"""
        self.source = source
        self.dest = dest


def move_node(source, dest):
    """move_node function"""
    if source is None:
        raise ValueError

    new_head = source
    source = source.next
    new_head.next = dest
    dest = new_head

    return Context(source, dest)
