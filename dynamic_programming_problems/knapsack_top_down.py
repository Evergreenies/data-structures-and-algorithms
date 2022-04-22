"""
Knapsack problem using top-down approach
"""
from typing import List, Any


def knapsack(weight: List[Any], value: List[Any], capacity: int | float, size: int) -> int | float:
    """
    Knapsack problem using TOP-DOWN approach

    :param weight:
    :type weight:
    :param value:
    :type value:
    :param capacity:
    :type capacity:
    :param size:
    :type size:
    :return:
    :rtype:
    """
    dp_table = [[0 for _ in range(capacity + 1)] for _ in range(size + 1)]

    for ni in range(size + 1):
        for wj in range(capacity + 1):
            if wt[ni - 1] <= wj:
                dp_table[ni][wj] = max(
                    value[ni - 1] + dp_table[ni - 1][wj - weight[ni - 1]],
                    dp_table[ni - 1][wj]
                )
            else:
                dp_table[ni][wj] = dp_table[ni - 1][wj]

    return dp_table[size][capacity]


if __name__ == '__main__':
    wt = [1, 3, 4, 5]
    val = [1, 4, 5, 7]
    n, w = 4, 7
    print(knapsack(wt, val, w, n))

    wt = [3, 4, 6, 5]
    val = [2, 3, 1, 4]
    n, w = 4, 8
    print(knapsack(wt, val, w, n))
