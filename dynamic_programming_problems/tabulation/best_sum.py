"""
Write a function `best_sum(target_sum, numbers)` that takes target_sum and array of numbers
as an argument.

The function should return an array containing the shortest combination of number that adds
up to exactly to the target_sum.

If there is tie for shortest combination, you may return one of them.
"""
from typing import List


def best_sum(target_sum: int, numbers: List) -> List | None:
    dp_table = [None for _ in range(target_sum + 1)]
    dp_table[0] = []  # noqa

    for index in range(target_sum):
        if dp_table[index] is not None:
            for num in numbers:
                combinations = [*dp_table[index], num]
                if ((index + num) <= target_sum) \
                        and ((not dp_table[index + num]) or (len(dp_table[index + num]) > len(combinations))):
                    dp_table[index + num] = combinations
    return dp_table[target_sum]


if __name__ == '__main__':
    print(best_sum(7, [5, 3, 4, 7]))
    print(best_sum(8, [2, 3, 5]))
    print(best_sum(8, [1, 4, 5]))
    print(best_sum(100, [1, 2, 5, 25]))
