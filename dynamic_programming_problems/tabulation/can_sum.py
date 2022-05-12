"""
Write a function `can_sum(target_sum, numbers)` that takes in the target sum and array of numbers.

The function should return boolean indicating whether it is possible to target sum using numbers
from the array.

You may use an element from array as many times as needed.
You may assume that all inputs as non-negative.
"""
from typing import List


def can_sum(target_sum: int, numbers: List) -> bool:
    """
    Function returning boolean whether target_sum could be achieved by adding array elements.

    :param target_sum:
    :type target_sum:
    :param numbers:
    :type numbers:
    :return:
    :rtype:
    """
    dp_table = [False for _ in range(target_sum + 1)]
    dp_table[0] = True

    for index in range(target_sum):
        if dp_table[index] is True:
            for num in numbers:
                if (index + num) <= target_sum:
                    dp_table[index + num] = True

    return dp_table[target_sum]


if __name__ == '__main__':
    print(can_sum(7, [2, 3]))
    print(can_sum(7, [5, 3, 4, 6]))
    print(can_sum(7, [2, 4]))
    print(can_sum(8, [2, 3, 5]))
    print(can_sum(300, [7, 14]))
