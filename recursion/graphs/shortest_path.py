"""
Shortest path algorithm
"""
from typing import List, Tuple

from recursion.graphs.graph_utilities import build_graph


def shortest_path(edges: List, source: str, destination: str) -> Tuple[int, str]:
    """
    Find shortest path

    :param edges:
    :type edges:
    :param source:
    :type source:
    :param destination:
    :type destination:
    :return:
    :rtype:
    """
    graph = build_graph(edges)
    visited, queue = {source}, [[source, 0, source]]  # noqa queue=[[source, distance, path]]

    while len(queue) > 0:
        current, distance, path = queue.pop(0)

        if current == destination:
            return distance, path

        for neighbour in graph[current]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append([neighbour, (distance + 1), f'{path}-->{neighbour}'])
    return -1, ''


if __name__ == '__main__':
    edg = [
        ['w', 'x'],
        ['x', 'y'],
        ['z', 'y'],
        ['z', 'v'],
        ['w', 'v'],
    ]
    print(shortest_path(edg, 'w', 'z'))
    print(shortest_path(edg, 'z', 'a'))
