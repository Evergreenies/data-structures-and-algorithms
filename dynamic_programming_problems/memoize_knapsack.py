"""
Memoization of knapsack
"""
from typing import List


def knapsack(wt: List[int], val: List[int], weight: int, n: int) -> int:
    """Knapsack by using memoization"""

    dp_table = [[-1 for _ in range(weight + 1)] for _ in range(n + 1)]
    if (n == 0) or (weight == 0):
        return 0

    if dp_table[n][weight] != -1:
        return dp_table[n][weight]

    if wt[n - 1] <= weight:
        dp_table[n][weight] = max(
            val[n - 1] + knapsack(wt, val, weight - wt[n - 1], n - 1),
            knapsack(wt, val, weight, n - 1)
        )
        return dp_table[n][weight]
    elif wt[n - 1] > weight:
        dp_table[n][weight] = knapsack(wt, val, weight, n - 1)
        return dp_table[n][weight]
    else:
        return -1


if __name__ == '__main__':
    _n, w = 4, 7
    _wt = [1, 3, 4, 5]
    _val = [1, 4, 5, 7]
    print(knapsack(_wt, _val, w, _n))
