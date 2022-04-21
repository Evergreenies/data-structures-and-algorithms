"""
Undirected Graph
"""
from typing import List, Dict, Set

from recursion.graphs.graph_utilities import build_graph


def undirected_graph(edges: List, source: str, destination: str) -> bool:
    """
    Undirected graph with cyclic scenarios

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
    return has_path(graph, source, destination, visited=set())


def has_path(graph: Dict, source: str, destination: str, visited: Set) -> bool:
    """
    Check whether path from source to target is exists or not.

    :param graph:
    :type graph:
    :param source:
    :type source:
    :param destination:
    :type destination:
    :param visited:
    :type visited:
    :return:
    :rtype:
    """
    if source == destination:
        return True

    if source in visited:
        return False

    visited.add(source)
    for neighbour in graph[source]:
        if has_path(graph, neighbour, destination, visited) is True:
            return True
    return False


if __name__ == '__main__':
    edg = [
        ['i', 'j'],
        ['k', 'i'],
        ['m', 'k'],
        ['k', 'l'],
        ['o', 'n'],
    ]
    assert undirected_graph(edg, 'j', 'm') is True
