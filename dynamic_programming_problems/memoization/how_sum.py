"""
Write a function how_sum(arr, target_sum)

The function should return an array containing any combinations of element that adds up to
exactly the target_sum. If there is not any combinations that adds up, then return None.

If there are multiple combinations then you may return any singe one.
"""
from typing import List, Dict


def how_sum(arr: List, target_sum: int, memoize: Dict) -> List | None:
    """
    Finding subset which produces target_sum

    :param arr:
    :type arr:
    :param target_sum:
    :type target_sum:
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

    for num in arr:
        reminder = target_sum - num
        result = how_sum(arr, reminder, memoize)
        if result is not None:
            memoize[target_sum] = [*result, num]
            return memoize[target_sum]

    memoize[target_sum] = None
    return memoize[target_sum]


if __name__ == '__main__':
    print(how_sum([2, 3], 7, {}))
    print(how_sum([5, 3, 4, 7], 7, {}))
    print(how_sum([2, 4], 7, {}))
    print(how_sum([2, 3, 5], 8, {}))
    print(how_sum([7, 14], 300, {}))
