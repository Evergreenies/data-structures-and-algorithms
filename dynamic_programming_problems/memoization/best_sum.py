"""
Write a function best_sum(target_sum, arr).

The function should return an array containing the shortest combination of numbers that adds up
to exactly the target sum.

If there is a tie for shortest combination, you may return any from shortest.
"""
from typing import List, Dict


def best_sum(target_sum: int, arr: List, memoize: Dict) -> List | None:
    """
    Finding best sum

    :param target_sum:
    :type target_sum:
    :param arr:
    :type arr:
    :param memoize:
    :type memoize:
    :return:
    :rtype:
    """
    if target_sum in memoize:
        return memoize[target_sum]

    if target_sum == 0:
        return []

    if target_sum < 0:
        return None

    shortest_combination = None
    for num in arr:
        reminder = target_sum - num
        reminder_combination = best_sum(reminder, arr, memoize)

        if reminder_combination is not None:
            combination = [*reminder_combination, num]

            if (shortest_combination is None) or (len(combination) < len(shortest_combination)):
                shortest_combination = combination

    memoize[target_sum] = shortest_combination
    return shortest_combination


if __name__ == '__main__':
    print(best_sum(7, [5, 3, 4, 7], {}))
    print(best_sum(8, [2, 3, 5], {}))
    print(best_sum(8, [1, 4, 5], {}))
    print(best_sum(100, [1, 2, 5, 25], {}))
