"""
Delete middle element of stack
"""

from typing import List


def delete_mid(arr: List, size: int, current: int) -> None:  # noqa
    """
    Deleting middle element of stack

    :param current:
    :type current:
    :param arr:
    :type arr:
    :param size:
    :type size:
    :return:
    :rtype:
    """

    # Skip the execution once current counter reached equal to the size of stack
    if (len(arr) == 0) or (current == size):
        return

    # Remove top element from stack and recurse the function
    temp = arr.pop()
    delete_mid(arr, size, current + 1)  # Increase counter to shrink input

    # Don't insert value to the stack if its middle value of stack
    if current != (size // 2):
        arr.insert(0, temp)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    delete_mid(arr, len(arr), 0)
    print(arr)
