"""
Program to sort a stack by using recursion technique
"""
from typing import List


def stack_sorting(stack: List) -> None:
    """
    Sorting a stack using recursion

    :param stack:
    :type stack:
    :return:
    :rtype:
    """

    if len(stack) == 1:
        return

    temp = stack.pop()
    stack_sorting(stack)
    insert(stack, temp)


def insert(stack: List, temp: int) -> None:
    """
    Insert element at desired position

    :param stack:
    :type stack:
    :param temp:
    :type temp:
    :return:
    :rtype:
    """

    # If last element is less than temp
    if (len(stack) == 0) or (stack[-1] <= temp):
        stack.insert(0, temp)
        return

    # If last element greater than the temp
    val = stack.pop()
    insert(stack, temp)
    stack.insert(0, val)


if __name__ == '__main__':
    arr = [0, 1, 2, 5]
    stack_sorting(arr)
    print(arr)
