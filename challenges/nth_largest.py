"""
nth or kth largest element
"""
import math
from typing import List, Set


def largest(arr: List, visited: Set) -> int:
    """
    Get the largest number by ignoring duplicate numbers

    :param arr:
    :type arr:
    :param visited:
    :type visited:
    :return:
    :rtype:
    """
    large = -math.inf
    for num in arr:
        if num in visited:
            continue

        if num > large:
            large = num
    return large


def nth_largest(target: int, arr: List, visited: Set, large: int, current: int = 0) -> int:
    """
    Program to find nth largest number in given array.

    :param target:
    :type target:
    :param arr:
    :type arr:
    :param visited:
    :type visited:
    :param large:
    :type large:
    :param current:
    :type current:
    :return:
    :rtype:
    """
    if current == target:
        return large

    large = largest(arr, visited)
    if large not in visited:
        visited.add(large)
    current += 1

    return nth_largest(target, arr, visited, large, current)


if __name__ == '__main__':
    array = [23, 2, 1, 0, 5, 6, 6, 6, 4]
    nth = 3
    print(nth_largest(nth, array, set(), 0, 0))
