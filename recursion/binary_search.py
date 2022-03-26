"""
Binary search problem using recursion.
"""
from typing import List


def binary_search(arr: List[int], left: int, right: int, target: int) -> int:
    """
    Binary search using recursion

    :param arr:
    :type arr:
    :param left:
    :type left:
    :param right:
    :type right:
    :param target:
    :type target:
    :return:
    :rtype:
    """

    if left > right:
        return -1

    mid = (left + right) // 2

    if target == arr[mid]:
        return mid

    if target < arr[mid]:
        return binary_search(arr, left, mid - 1, target)

    return binary_search(arr, mid + 1, right, target)


if __name__ == '__main__':
    array = [index for index in range(20)]
    print(binary_search(array, 0, len(array) - 1, 16))
