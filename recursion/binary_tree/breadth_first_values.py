"""
Binary Tree using breadth first values
"""
from typing import List, Any

from recursion.binary_tree.tree_node import BinaryTree, build_tree


def iterative_binary_tree_values(root: BinaryTree) -> List[Any]:
    """
    Iterative BFS solution to print binary tree values
    :param root:
    :type root:
    :return:
    :rtype:
    """
    if root is None:
        return []

    queue, result = [root], []
    while len(queue) > 0:
        current = queue.pop(0)
        result.append(current.val)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return result


if __name__ == '__main__':
    nodes = ['a', 'b', 'c', 'd', 'e', 'f']
    tree_root = build_tree(nodes)
    print(iterative_binary_tree_values(tree_root))
    # print(recursive_depth_first_value(tree_root))
