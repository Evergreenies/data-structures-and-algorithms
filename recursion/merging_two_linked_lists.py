"""
Merging two linked lists by recursive approach
"""


class Node(object):
    """Node of linked lists"""

    def __init__(self, val, next_node=None):
        self.val = val
        self.next_node = next_node


def merge(node1: Node, node2: Node) -> Node:
    """
    Merge two linked lists

    :param node1:
    :type node1:
    :param node2:
    :type node2:
    :return:
    :rtype:
    """
    if not node1:
        return node2
    if not node2:
        return node1

    if node1.val < node2.val:
        node1.next_node = merge(node1.next_node, node2)
        return node1
    else:
        node2.next_node = merge(node1, node2.next_node)
        return node2


def print_list(head: Node) -> None:
    """Print Linked Lists"""
    itr = head
    while itr:
        print(itr.val)
        itr = itr.next_node


if __name__ == '__main__':
    n1_1 = Node(1)
    n1_2 = Node(5)
    n1_3 = Node(13)
    n1_4 = Node(14)
    n1_5 = Node(550)

    n1_1.next_node = n1_2
    n1_2.next_node = n1_3
    n1_3.next_node = n1_4
    n1_4.next_node = n1_5

    n2_1 = Node(2)
    n2_2 = Node(15)
    n2_3 = Node(130)
    n2_4 = Node(200)
    n2_5 = Node(350)

    n2_1.next_node = n2_2
    n2_2.next_node = n2_3
    n2_3.next_node = n2_4
    n2_4.next_node = n2_5
    print_list(merge(n1_1, n2_1))
