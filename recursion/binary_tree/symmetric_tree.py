"""
Symmetric Tree
"""
from recursion.binary_tree.tree_node import Node


def explore(left_tree: Node, right_tree: Node) -> bool:
    """
    Explore the tree left as well as right side

    :param left_tree:
    :type left_tree:
    :param right_tree:
    :type right_tree:
    :return:
    :rtype:
    """
    if (left_tree is None) and (right_tree is None):
        return True
    if ((left_tree is None) != (right_tree is None)) or (left_tree.val != right_tree.val):
        return False
    return explore(left_tree.left, right_tree.right) and explore(left_tree.right, right_tree.left)


def is_symmetric(root: Node) -> bool:
    """
    Check whether tree symmetric or not.

    :param root:
    :type root:
    :return:
    :rtype:
    """
    if root is None:
        return True
    return explore(root.left, root.right)


if __name__ == '__main__':
    root_node = Node(4)

    left_node_5 = Node(5)
    left_node_2 = Node(2)
    left_node_7 = Node(7)
    left_node_9 = Node(9)
    left_node_7_1 = Node(7)
    left_node_1 = Node(1)
    left_node_3 = Node(3)
    left_node_0 = Node(0)
    left_node_6 = Node(6)

    right_node_5 = Node(5)
    right_node_2 = Node(2)
    right_node_7 = Node(7)
    right_node_9 = Node(9)
    right_node_7_1 = Node(7)
    right_node_1 = Node(1)
    right_node_3 = Node(3)
    right_node_0 = Node(0)
    right_node_6 = Node(6)

    # Left tree assignment
    root_node.left = left_node_5

    left_node_5.left = left_node_2
    left_node_5.right = left_node_7

    left_node_2.left = left_node_9
    left_node_2.right = left_node_7_1

    left_node_7.left = left_node_1

    left_node_9.left = left_node_3
    left_node_9.right = left_node_0

    left_node_7_1.right = left_node_6

    # Right tree assignment
    root_node.right = right_node_5

    right_node_5.right = right_node_2
    right_node_5.left = right_node_7

    right_node_2.right = right_node_9
    right_node_2.left = right_node_7_1

    right_node_7.right = right_node_1

    right_node_9.right = right_node_3
    right_node_9.left = right_node_0

    right_node_7_1.left = right_node_6

    print(is_symmetric(root_node))

    # Second example
    root_node = Node(4)

    left_node_5 = Node(5)
    left_node_2 = Node(2)
    left_node_7 = Node(7)
    left_node_9 = Node(9)
    left_node_7_1 = Node(7)
    left_node_1 = Node(1)
    left_node_3 = Node(3)
    left_node_0 = Node(0)
    left_node_6 = Node(6)

    right_node_5 = Node(5)
    right_node_2 = Node(2)
    right_node_7 = Node(7)
    right_node_9 = Node(9)
    right_node_7_1 = Node(7)
    right_node_1 = Node(1)
    right_node_3 = Node(3)
    right_node_0 = Node(0)
    right_node_6 = Node(6)
    right_node_11 = Node(11)

    # Left tree assignment
    root_node.left = left_node_5

    left_node_5.left = left_node_2
    left_node_5.right = left_node_7

    left_node_2.left = left_node_9
    left_node_2.right = left_node_7_1

    left_node_7.left = left_node_1

    left_node_9.left = left_node_3
    left_node_9.right = left_node_0

    left_node_7_1.right = left_node_6

    # Right tree assignment
    root_node.right = right_node_5

    right_node_5.right = right_node_2
    right_node_5.left = right_node_7

    right_node_2.right = right_node_9
    right_node_2.left = right_node_7_1

    right_node_7.right = right_node_1
    right_node_7.left = right_node_11

    right_node_9.right = right_node_3
    right_node_9.left = right_node_0

    right_node_7_1.left = right_node_6

    print(is_symmetric(root_node))
