"""
Calculate num of graphs
"""
from typing import Dict, Set


def connected_component_count(graph: Dict) -> int:
    """
    Count number of graphs exists

    :param graph:
    :type graph:
    :return:
    :rtype:
    """
    count, visited = 0, set()
    for node in graph:
        if explore(graph, node, visited) is True:
            count += 1
    return count


def explore(graph: Dict, current: int, visited: Set) -> bool:
    """
    Explore the current node b their all neighbours.

    :param graph:
    :type graph:
    :param current:
    :type current:
    :param visited:
    :type visited:
    :return:
    :rtype:
    """
    if current in visited:
        return False
    visited.add(current)
    for neighbour in graph[current]:
        explore(graph, neighbour, visited)
    return True


if __name__ == '__main__':
    grh = {
        0: [8, 1, 5],
        1: [0],
        5: [0, 8],
        8: [0, 5],
        2: [3, 4],
        3: [2, 4],
        4: [3, 2],
    }
    assert connected_component_count(grh) == 2
