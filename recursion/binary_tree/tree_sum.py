"""
Calculater sum of all tree values
"""
from recursion.binary_tree.tree_node import Node


def recursive_dfs_tree_sum(root: Node) -> int | float:
    """
    Recursive DFS solution to calculate sum of all tree values.

    :param root:
    :type root:
    :return:
    :rtype:
    """

    if root is None:
        return 0

    total = root.val
    left_sum = recursive_dfs_tree_sum(root.left)
    right_sum = recursive_dfs_tree_sum(root.right)
    return total + left_sum + right_sum


if __name__ == '__main__':
    root_node = Node(3)
    node_11 = Node(11)
    node_4 = Node(4)
    node_4r = Node(4)
    node_2 = Node(-2)
    node_1 = Node(1)

    root_node.left = node_11
    root_node.right = node_4r

    node_11.left = node_4
    node_11.right = node_2
    node_4r.right = node_1

    assert recursive_dfs_tree_sum(root_node) == 21
