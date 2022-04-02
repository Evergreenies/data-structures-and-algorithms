"""
Josephus Problem OR Game of Death in circle

EX -
INPUTS:
    N = 40
    K = 7

OUTPUT:
    24

"""
from typing import List


def game_of_dath(arr: List, k: int, current: int) -> int:  # noqa
    if len(arr) == 1:
        return arr[0]

    target = (current + k) % len(arr)
    arr.pop(target)
    game_of_dath(arr, k, target)
    return arr[0]


if __name__ == '__main__':
    number_of_elements = 40
    steps_to_target = 7
    arr = [idx for idx in range(1, number_of_elements + 1)]

    start_from = 0
    assert game_of_dath(arr, steps_to_target - 1, start_from) == 24
