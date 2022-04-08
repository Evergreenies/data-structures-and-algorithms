"""
Implementing DFS graph traversal
"""
from typing import Dict


def recursive_dfs_traversal(graph: Dict, source: str) -> None:
    """
    Recursive solution for DFS graph traversal

    :param graph:
    :type graph:
    :param source:
    :type source:
    :return:
    :rtype:
    """
    print(source)
    for neighbour in graph[source]:
        recursive_dfs_traversal(graph, neighbour)


if __name__ == '__main__':
    gph = {
        'a': ['b', 'c'],
        'b': ['d'],
        'c': ['e'],
        'd': ['f'],
        'e': [],
        'f': [],
    }
    recursive_dfs_traversal(gph, 'a')
