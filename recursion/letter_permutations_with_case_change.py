"""
Letter permutation combination with case of alphanumeric string

Ex -
Input - '1a1B2'
Output - ['1a1b2', '1a1B2', '1A1b2', '1A1B2']
"""
from typing import List


def permutations(inp: str, op: str, arr: List) -> None:  # noqa
    """
    Finding all permutations

    :param inp:
    :type inp:
    :param op:
    :type op:
    :param arr:
    :type arr:
    :return:
    :rtype:
    """
    if len(inp) == 0:
        arr.append(op)
        return

    op1 = op
    # Check whether current character is string or digit. If digit, reduce input and start single recursive call
    if inp[0].isdigit():
        op1 = op1 + inp[0]
        inp = inp[1:]
        permutations(inp, op1, arr)
        return

    op2 = op
    op1 = op1 + inp[0].lower()
    op2 = op2 + inp[0].upper()

    inp = inp[1:]
    permutations(inp, op1, arr)
    permutations(inp, op2, arr)


if __name__ == '__main__':
    arr = []
    permutations('a1B2', '', arr)
    print(arr)
