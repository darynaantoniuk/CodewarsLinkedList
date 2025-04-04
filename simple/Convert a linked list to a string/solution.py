"""convert a linked list to a string"""



class Node():
    """class node"""
    def __init__(self, data, next = None):
        self.data = data
        self.next = next




def stringify(node):
    """stringify"""
    res_str = ""
    if node is None:
        return "None"
    while node is not None:
        res_str += str(node.data)
        node = node.next
        if node is None:
            res_str += " -> None"
            break
        res_str += " -> "
    return res_str

print(stringify(Node(0, Node(1, Node(2, Node(3))))))
