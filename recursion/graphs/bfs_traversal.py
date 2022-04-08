"""
BFS:
"""
from typing import Dict


def bfs_traversal(graph: Dict, source: str) -> None:
    """
    Function to traverse the graph using BFS manner.

    :param graph:
    :type graph:
    :param source:
    :type source:
    :return:
    :rtype:
    """
    queue = [source]
    while len(queue) > 0:
        current = queue.pop(0)
        print(current)

        for neighbour in graph[current]:
            bfs_traversal(graph, neighbour)


if __name__ == '__main__':
    gph = {
        'a': ['c', 'd'],
        'b': ['d'],
        'c': ['e'],
        'd': ['f'],
        'e': [],
        'f': [],
    }
    bfs_traversal(gph, 'a')
