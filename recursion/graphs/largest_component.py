"""
Find component with large size
"""
from typing import Dict, Set


def largest_component(graph: Dict) -> int:
    """
    Largest component

    :param graph:
    :type graph:
    :return:
    :rtype:
    """
    largest, visited = 0, set()

    for node in graph:
        size = explore(graph, node, visited)
        if size > largest:
            largest = size

    return largest


def explore(graph: Dict, node: int, visited: Set) -> int:
    """
    Exploring all neighbours of current node

    :param graph:
    :type graph:
    :param node:
    :type node:
    :param visited:
    :type visited:
    :return:
    :rtype:
    """
    if node in visited:
        return 0

    visited.add(node)
    size = 1

    for neighbour in graph[node]:
        size += explore(graph, neighbour, visited)

    return size


if __name__ == '__main__':
    grp = {
        0: [8, 1, 5],
        1: [0],
        5: [0, 8],
        8: [0, 5],
        2: [3, 4],
        3: [2, 4],
        4: [3, 2],
    }
    assert largest_component(grp) == 4
