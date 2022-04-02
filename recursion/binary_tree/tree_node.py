"""
Common utilities being used in tree classes
"""
from typing import List, Any


class Node(object):
    """A Node"""

    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree(Node):
    """Abstract Binary Tree"""

    def __init__(self, val=None, left=None, right=None):
        super(BinaryTree, self).__init__(val, left, right)

    def insert(self, val: int) -> None:
        """
        Insert the node

        :param val:
        :type val:
        :return:
        :rtype:
        """
        if val == self.val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
            else:
                self.left = BinaryTree(val)
        else:
            if self.right:
                self.right.insert(val)
            else:
                self.right = BinaryTree(val)


def build_tree(elements: List[Any]) -> BinaryTree:
    """
    Build tree by inserting list of element in it

    :param elements:
    :type elements:
    :return:
    :rtype:
    """
    root = BinaryTree(elements[0])

    for i in range(1, len(elements)):
        root.insert(elements[i])

    return root
