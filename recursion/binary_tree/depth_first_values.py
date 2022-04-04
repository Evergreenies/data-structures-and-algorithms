"""
Depth First Values

Write a function `depth_first_values`, that takes in the root of binary tree. The function
should return an array containing all values of the tree in DFS order.
"""
from typing import List, Any

from recursion.binary_tree.tree_node import BinaryTree, build_tree


def iterative_depth_first_value(root: BinaryTree) -> List:
    """
    Print binary tree values by using DFS

    :param root:
    :type root:
    :return:
    :rtype:
    """
    if root is None:
        return []

    stack, result = [root], []
    while len(stack) > 0:
        current = stack.pop()
        result.append(current.val)

        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return result


def recursive_depth_first_value(root: BinaryTree) -> List[Any]:
    """
    Print binary tree values using DFS recursive solution

    :param root:
    :type root:
    :return:
    :rtype:
    """
    if root is None:
        return []
    left_sub_tree = recursive_depth_first_value(root.left)
    right_sub_tree = recursive_depth_first_value(root.right)
    return [root.val, *left_sub_tree, *right_sub_tree]


if __name__ == '__main__':
    nodes = ['a', 'b', 'c', 'd', 'e', 'f']
    tree_root = build_tree(nodes)
    print(iterative_depth_first_value(tree_root))
    print(recursive_depth_first_value(tree_root))
