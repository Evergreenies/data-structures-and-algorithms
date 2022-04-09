"""
Has Path

Write a function `has_path` that takes in an object representing the adjacency list of a directed cyclic graph
and two nodes (src, dst). The function should return boolean representing whether there exist path between
the source and the destination nodes.
"""
from typing import Dict


def recursive_dfs_has_path(graph: Dict, source: str, destination: str) -> bool:
    """
    Recursive DFS solution to find whether path to the destination is exists or not.

    :param graph:
    :type graph:
    :param source:
    :type source:
    :param destination:
    :type destination:
    :return:
    :rtype:
    """
    if source == destination:
        return True

    for neighbour in graph[source]:
        if recursive_dfs_has_path(graph, neighbour, destination) is True:
            return True
    return False


def iterative_dfs_has_path(graph: Dict, source: str, destination: str) -> bool:
    """
    Iterative DFS solution to find whether path to target exists or not.

    :param graph:
    :type graph:
    :param source:
    :type source:
    :param destination:
    :type destination:
    :return:
    :rtype:
    """

    stack = [source]
    while len(stack) > 0:
        current = stack.pop()

        if current == destination:
            return True

        for neighbour in graph[current]:
            stack.append(neighbour)

    return False


def iterative_bfs_has_path(graph: Dict, source: str, destination: str) -> bool:
    """
    Iterative BFS solution to find whether path to target exists or not.

    :param graph:
    :type graph:
    :param source:
    :type source:
    :param destination:
    :type destination:
    :return:
    :rtype:
    """
    queue = [source]
    while len(queue) > 0:
        current = queue.pop(0)

        if current == destination:
            return True

        for neighbour in graph[current]:
            queue.append(neighbour)

    return False


if __name__ == '__main__':
    grh = {
        'f': ['g', 'i'],
        'g': ['h'],
        'h': [],
        'i': ['g', 'k'],
        'j': ['i'],
        'k': [],
    }
    assert recursive_dfs_has_path(grh, 'f', 'k') is True
    assert recursive_dfs_has_path(grh, 'f', 'x') is False

    assert iterative_dfs_has_path(grh, 'f', 'k') is True
    assert iterative_dfs_has_path(grh, 'f', 'x') is False

    assert iterative_bfs_has_path(grh, 'f', 'k') is True
    assert iterative_bfs_has_path(grh, 'j', 'i') is True
