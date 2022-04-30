"""
Write a function `can_sum(target_sum, arr)`.
The function should return boolean indicating whether is it possible to generate target_sum
using numbers from the array.
"""
from typing import List, Dict


def can_sum(arr: List, target_sum: int, memoize: Dict) -> bool:
    """
    This function returns True/False indicating whether it is possible to generate target_sum

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
        return True

    if target_sum < 0:
        return False

    for num in arr:
        reminder = target_sum - num
        if can_sum(arr, reminder, memoize) is True:
            memoize[target_sum] = True
            return memoize[target_sum]

    memoize[target_sum] = False
    return memoize[target_sum]


if __name__ == '__main__':
    print(can_sum([2, 3], 7, {}))
    print(can_sum([5, 3, 4, 7], 7, {}))
    print(can_sum([2, 4], 7, {}))
    print(can_sum([2, 3, 5], 8, {}))
    print(can_sum([7, 14], 300, {}))
