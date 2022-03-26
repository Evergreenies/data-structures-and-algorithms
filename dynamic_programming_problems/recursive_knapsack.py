"""
Knapsack in recursive manner.
"""
from typing import List


def recursive_knapsack(wt: List[int], val: List, weight: int, length: int) -> int:
    """
    Knapsack using recursion

    :param wt:
    :type wt:
    :param val:
    :type val:
    :param weight:
    :type weight:
    :param length:
    :type length:
    :return:
    :rtype:
    """
    if (length == 0) or (weight == 0):
        return 0

    if wt[length - 1] <= weight:
        return max(
            val[length-1] + recursive_knapsack(wt, val, weight - wt[length-1], length - 1),
            recursive_knapsack(wt, val, weight, length - 1)
        )
    elif wt[length-1] > weight:
        return recursive_knapsack(wt, val, weight, length - 1)
    else:
        return -1


if __name__ == '__main__':
    n, w = 4, 7
    _wt = [1, 3, 4, 5]
    _val = [1, 4, 5, 7]
    print(recursive_knapsack(_wt, _val, w, n))

