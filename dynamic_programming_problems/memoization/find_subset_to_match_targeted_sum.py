"""
Find whether the subset as sum of all elements is equal to the target exists in given array or not.
"""
from typing import List


def find_subset_with_target_sum(arr: List, target: int | float) -> bool:
    """
    Find subsets from given set

    :param arr:
    :type arr:
    :param target:
    :type target:
    :return:
    :rtype:
    """
    dp_table = [[(False if ((j == 0) and i != 0) else True) for i in range(target + 1)] for j in range(len(arr) + 1)]

    for ni in range(len(arr) + 1):
        for wj in range(target + 1):
            if arr[ni-1] <= wj:
                dp_table[ni][wj] = dp_table[ni][wj - arr[ni - 1]] or dp_table[ni - 1][wj]
            else:
                dp_table[ni][wj] = dp_table[ni - 1][wj]

    return dp_table[len(arr)][target]


if __name__ == '__main__':
    print(find_subset_with_target_sum([2, 3, 7, 8, 10], 11))
