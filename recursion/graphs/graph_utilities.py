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

        if not (a in graph):
            graph[a] = []
        if not (b in graph):
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)

    return graph
