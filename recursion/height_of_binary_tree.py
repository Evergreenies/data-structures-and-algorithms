"""
Program to find height of binary tree
"""
from typing import List


class Node(object):
    """Node of tree"""

    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree(Node):
    """Binary Tree"""

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

    def inoder(self) -> List[int]:
        """
        Inorder traversal of tree
        :return:
        :rtype:
        """

        elements = []
        if self.left:
            elements += self.left.inoder()
        elements.append(self.val)
        if self.right:
            elements += self.right.inoder()
        return elements

    def height(self, root: Node) -> int:
        """
        Height of binary tree

        :param root:
        :type root:
        :return:
        :rtype:
        """
        if root is None:
            return 0

        left_height = self.height(root.left)
        right_height = self.height(root.right)
        return 1 + max(left_height, right_height)

    @staticmethod
    def print_leaves(root) -> None:
        """
        Print only leaf nodes of the tree

        :param root:
        :type root:
        :return:
        :rtype:
        """
        if root is None:
            return

        # Check if current node is leaf node
        if root.left is None or root.right is None:
            print(root.val)
            return

        # Explore left subtree
        if root.left is not None:
            root.print_leaves(root.left)

        # Explore right subtree
        if root.right is not None:
            root.print_leaves(root.right)


def build_tree(elements: List[int]) -> BinaryTree:
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


if __name__ == '__main__':
    tree_root = build_tree([4, 2, 5, 1, 3, 0])
    print("INORDER: ", tree_root.inoder())
    print(f"HEIGHT: {tree_root.height(tree_root)}")
    print("LEAVES:")
    tree_root.print_leaves(tree_root)

    tree_root = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print("INORDER: ", tree_root.inoder())
    print(f"HEIGHT: {tree_root.height(tree_root)}")
    print("LEAVES:")
    tree_root.print_leaves(tree_root)
