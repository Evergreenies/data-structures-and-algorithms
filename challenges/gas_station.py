"""
Given a circular list of gas stations, where we can go from a station i to the
station i+1, and the last one goes to the first one, find the index of the
station from where we start to be able to traverse all the stations and go back
to the initial one without running out of gas.
"""
from typing import List


def can_traverse(_gas: List, _cost: List, start: int) -> bool:
    """
    Traverse through all stations just to check whether we can traverse.

    :param _gas:
    :type _gas:
    :param _cost:
    :type _cost:
    :param start:
    :type start:
    :return:
    :rtype:
    """
    size, remaining, index = len(_gas), 0, start

    started = False
    while (index != start) or (not started):
        started = True
        remaining += (_gas[index] - _cost[index])

        if remaining < 0:
            return False
        index = (index + 1) % size

    return True


def gas_station(_gas: List, _cost: List) -> int:
    """
    Gas Station

    :param _gas:
    :type _gas:
    :param _cost:
    :type _cost:
    :return:
    :rtype:
    """
    for index in range(len(_gas)):
        if can_traverse(_gas, _cost, index):
            return index
    return -1


if __name__ == '__main__':
    gas = [1, 5, 3, 3, 5, 3, 1, 3, 4, 5]
    cost = [5, 2, 2, 8, 2, 4, 2, 5, 1, 2]
    print(gas_station(gas, cost))
