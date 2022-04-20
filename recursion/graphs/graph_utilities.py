from typing import List, Dict


def build_graph(edges: List) -> Dict:
    """
    Returns adjacency list

    :param edges:
    :type edges:
    :return:
    :rtype:
    """
    graph = {}

    for edge in edges:
        a, b = edge

        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)

    return graph
