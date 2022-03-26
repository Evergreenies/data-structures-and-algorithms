"""
Print linked list in reverse order
"""


class Node(object):
    """Linked List Node"""

    def __init__(self, val=None, next_node=None):
        self.val = val
        self.next_node = next_node


class LinkedLists:
    """Linked List"""

    def __init__(self):
        self.head = None

    def reverse_list(self, head: Node) -> Node:
        """
        Reversing linked list

        :param head:
        :type head:
        :return:
        :rtype:
        """
        if (head == None) or (head.next_node == None):  # noqa
            return head

        current = self.reverse_list(head.next_node)
        head.next_node.next_node = head
        head.next_node = None
        return current


def print_list(head: Node) -> None:
    """Printing linked list"""

    itr = head
    while itr:
        print(itr.val)
        itr = itr.next_node


if __name__ == '__main__':
    linked_list = LinkedLists()

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)

    node1.next_node = node2
    node2.next_node = node3
    node3.next_node = node4
    node4.next_node = node5

    print_list(linked_list.reverse_list(node1))
