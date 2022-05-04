"""
Grid Traveller

Say that you are traveller on a 2D grid. You begin in the top-left corner and your goal is to travel
to the bottom right corner. You may only move down or right.

In how many ways you can travel to the goal on grid with dimensions M * N
"""
from typing import Dict


def grid_traveller(row: int, columns: int, memoize: Dict) -> int:
    """
    Grid traveller with memoization

    :param row:
    :type row:
    :param columns:
    :type columns:
    :param memoize:
    :type memoize:
    :return:
    :rtype:
    """

    # Look into the dict for existence of key to reduce recursion
    key = (row, columns)
    if memoize.get(key):
        return memoize[key]

    # If grid is single
    if (row == 1) and (columns == 1):
        return 1

    # If any row or columns reached to zero means there is no further way to travel
    if (row == 0) or (columns == 0):
        return 0

    memoize[key] = grid_traveller(row - 1, columns, memoize) + grid_traveller(row, columns - 1, memoize)
    return memoize[key]


if __name__ == '__main__':
    print(grid_traveller(1, 1, memoize={}))
    print(grid_traveller(2, 3, memoize={}))
    print(grid_traveller(3, 2, memoize={}))
    print(grid_traveller(3, 3, memoize={}))
    print(grid_traveller(18, 18, memoize={}))
