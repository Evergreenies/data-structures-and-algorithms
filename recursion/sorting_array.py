"""
Sort and array using recursion
"""
from typing import List


def sorting_array(arr: List) -> None:  # noqa
    """
    Array soring using recursion

    :param arr:
    :type arr:
    :return:
    :rtype:
    """
    # If array has just single value
    if len(arr) == 1:
        return

    # Store last element from array and store it as temp var
    temp = arr.pop()
    sorting_array(arr)

    # Swapping position of the last element at desired position
    insert(arr, temp)


def insert(arr: List, temp: int) -> None:  # noqa
    """
    Swapping elements at desired position

    :param arr:
    :type arr:
    :param temp:
    :type temp:
    :return:
    :rtype:
    """
    # If array length is zero of temp value is greater than last then append 
    # temp to array and return
    if (len(arr) == 0) or (arr[-1] <= temp):
        arr.append(temp)
        return

    # Remove last element if it is greater than the temp
    val = arr.pop()
    insert(arr, temp)
    arr.append(val)


if __name__ == '__main__':
    arr = [2, 3, 7, 6, 4, 5, 9]
    sorting_array(arr)
    print("SORTING: ", arr)
