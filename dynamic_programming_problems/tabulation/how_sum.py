"""
Write a function `how_sum(target_sum, numbers)` that takes target_sum and an array of
numbers as an argument.

The function should return an array containing any combinations of numbers that adds up
to exactly the target_sum.

Keep default return as None and you can return just single array even there are many
possibilities.
"""
from typing import List


def how_sum(target_sum: int, numbers: List) -> List | None:
    """

    :param target_sum:
    :type target_sum:
    :param numbers:
    :type numbers:
    :return:
    :rtype:
    """
    dp_table = [None for _ in range(target_sum + 1)]
    dp_table[0] = []  # noqa

    for item in range(target_sum):
        if dp_table[item] is not None:
            for num in numbers:
                if (item + num) <= target_sum:
                    dp_table[item + num] = [*dp_table[item], num]

    return dp_table[target_sum]


if __name__ == '__main__':
    print(how_sum(7, [2, 3]))
    print(how_sum(7, [5, 3, 4, 7]))
    print(how_sum(7, [2, 4]))
    print(how_sum(8, [2, 3, 5]))
    print(how_sum(300, [7, 14]))
