"""
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.
"""


def has_duplicates(arr: list, index: int = 0, visited: set = None) -> bool:
    """
    Check whether list contains duplicate elements.

    :param arr: array of elements
    :type arr: list
    :param index: current index
    :type index: int
    :param visited: visited elements
    :type visited: set
    :return: whether array has distinct elements or not
    :rtype: bool
    """

    if (not arr) or (len(arr) == 0) or (index > len(arr) - 1):
        return False

    if visited is None:
        visited = set()

    if arr[index] in visited:
        return True
    visited.add(arr[index])

    return has_duplicates(arr, index + 1, visited)


if __name__ == '__main__':
    assert has_duplicates([1, 2, 3, 4, 5, 6, 7, 8]) is False
    assert has_duplicates([1, 4, 5, 4, 0, 9]) is True
    assert has_duplicates([1]) is False
    assert has_duplicates([]) is False
