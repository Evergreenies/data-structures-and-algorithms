"""
Find minimum value from the array
"""
import math

from recursion.binary_tree.tree_node import BinaryTree, build_tree


def recursive_dfs_minimum_value(root: BinaryTree) -> int | float:
    """
    Find minimum value from tree by using recursive DFS

    :param root:
    :type root:
    :return:
    :rtype:
    """
    if root is None:
        return math.inf

    left_subtree_minimum = recursive_dfs_minimum_value(root.left)
    right_subtree_minimum = recursive_dfs_minimum_value(root.right)
    return min(root.val, left_subtree_minimum, right_subtree_minimum)


if __name__ == '__main__':
    elements = [5, 11, 3, 4, 15, 12]
    tree_root = build_tree(elements)
    assert recursive_dfs_minimum_value(tree_root) == 3

    elements = []
    tree_root = build_tree(elements)
    assert recursive_dfs_minimum_value(tree_root) == math.inf
