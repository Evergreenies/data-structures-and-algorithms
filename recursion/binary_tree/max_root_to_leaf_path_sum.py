"""
Max root to leaf path sum
"""
import math

from recursion.binary_tree.tree_node import build_tree, BinaryTree


def recursive_dfs_max_sum(root: BinaryTree) -> int | float:
    """
    Recursive solution to find maximum sum of tree path

    :param root:
    :type root:
    :return:
    :rtype:
    """
    if root is None:
        return -math.inf

    if (root.left is None) and (root.right is None):
        return root.val

    return root.val + max(
        recursive_dfs_max_sum(root.left),
        recursive_dfs_max_sum(root.right)
    )


if __name__ == '__main__':
    elements = [5, 11, 3, 4, 2, 1]
    tree_root = build_tree(elements)
    assert recursive_dfs_max_sum(tree_root) == 16
