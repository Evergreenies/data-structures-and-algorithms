"""
Given a sorted array of integers arr and an integer target, find the index of the
first and last position of target in array. If target not found in array return
[-1, -1]
"""
from typing import List


def find_first_and_last_index(target: int, arr: List) -> List:
    """
    Find the first and last index of array for the target provided.

    :param target:
    :type target:
    :param arr:
    :type arr:
    :return:
    :rtype:
    """
    for index, ele in enumerate(arr):
        if ele == target:
            start = index
            while ((index + 1) < len(arr)) and (arr[index + 1] == target):
                index += 1
            return [start, index]
    return [-1, -1]


"""
Recursive solution
"""


def left_to_right(target: int, arr: List, start: int, end: int) -> int:
    """
    Traverse towards right in array to find target element in array

    :param target:
    :type target:
    :param arr:
    :type arr:
    :param start:
    :type start:
    :param end:
    :type end:
    :return:
    :rtype:
    """
    if len(arr) == start:
        return -1
    if arr[start] == target:
        return start
    start += 1
    return left_to_right(target, arr, start, end)


def right_to_left(target: int, arr: List, start: int, end: int) -> int:
    """
    Traversing from right to left to find target element in array

    :param target:
    :type target:
    :param arr:
    :type arr:
    :param start:
    :type start:
    :param end:
    :type end:
    :return:
    :rtype:
    """
    if (arr[end] == target) or (start == end):
        return end
    end -= 1
    return right_to_left(target, arr, start, end)


def recursive(target: int, arr: List) -> List:
    """
    Recursive approach to find start and end index of target in sorted array
    :param target:
    :type target:
    :param arr:
    :type arr:
    :return:
    :rtype:
    """
    if len(arr) == 0:
        return [-1, -1]
    start_index = left_to_right(target, arr, start=0, end=(len(arr) - 1))
    if start_index == -1:  # If start_index is -1 it means we visited each element of array but target not found
        return [-1, -1]
    end_index = right_to_left(target, arr, start_index, end=(len(arr) - 1))
    return [start_index, end_index]


if __name__ == '__main__':
    print("Brute Force")
    print(find_first_and_last_index(5, [2, 4, 5, 5, 5, 5, 5, 7, 9, 9]))
    print(find_first_and_last_index(7, [2, 4, 5, 5, 5, 5, 5, 7, 9, 9]))
    print(find_first_and_last_index(-1, [-1, 0, 2, 4, 5, 5, 5, 5, 5, 7, 9, 9]))
    print(find_first_and_last_index(0, [0, 2, 4, 5, 5, 5, 5, 5, 7, 9, 9]))
    print(find_first_and_last_index(11, [2, 4, 5, 5, 5, 5, 5, 7, 9, 9]))

    print("Recursive approach")
    print(recursive(5, [2, 4, 5, 5, 5, 5, 5, 7, 9, 9]))
    print(recursive(-1, [-1, 0, 2, 4, 5, 5, 5, 5, 5, 7, 9, 9]))
    print(recursive(0, [0, 2, 4, 5, 5, 5, 5, 5, 7, 9, 9]))
    print(recursive(11, [2, 4, 5, 5, 5, 5, 5, 7, 9, 9]))
    print(recursive(6, [5, 7, 8, 8, 10]))
    print(recursive(2, [2, 2]))
    print(recursive(3, [3, 3, 3]))
    print(recursive(4, [1, 4]))
