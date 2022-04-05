"""
Find whether given element exist in tree or not using DFS, BFS, and DFS Recursive
"""
from typing import Any

from recursion.binary_tree.tree_node import BinaryTree, build_tree


def iterative_bfs_tree_include(root: BinaryTree, target: Any) -> bool:
    """
    Iterative BFS solution to find the target element exist in tree or not.

    :param root:
    :type root:
    :param target:
    :type target:
    :return:
    :rtype:
    """
    if root is None:
        return False
    queue = [root]
    while len(queue) > 0:
        current = queue.pop(0)

        if current.val == target:
            return True

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return False


def iterative_dfs_tree_include(root: BinaryTree, target: Any) -> bool:
    """
    Iterative DFS solution to find target element exist in tree or not

    :param root:
    :type root:
    :param target:
    :type target:
    :return:
    :rtype:
    """
    if root is None:
        return False

    stack = [root]
    while len(stack) > 0:
        current = stack.pop()

        if current.val == target:
            return True

        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

    return False


def recursive_dfs_tree_includes(root: BinaryTree, target: Any) -> bool:
    """
    Recursive DFS solution to find target element exit in tree or not.

    :param root:
    :type root:
    :param target:
    :type target:
    :return:
    :rtype:
    """
    if root is None:
        return False
    if root.val == target:
        return True
    recursive_dfs_tree_includes(root.left, target)
    recursive_dfs_tree_includes(root.right, target)
    return False


if __name__ == '__main__':
    nodes = ['a', 'b', 'c', 'd', 'e', 'f']
    tree_root = build_tree(nodes)

    assert iterative_bfs_tree_include(tree_root, 'e') is True
    assert iterative_bfs_tree_include(tree_root, 'h') is False

    assert iterative_dfs_tree_include(tree_root, 'e') is True
    assert iterative_dfs_tree_include(tree_root, 'z') is False

    assert recursive_dfs_tree_includes(tree_root, 'f') is False
    assert recursive_dfs_tree_includes(tree_root, 'y') is False
