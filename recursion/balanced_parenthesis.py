"""
Program to print balanced parenthesis
"""
from typing import List


def balanced_parenthesis(opn: int, close: int, output: str, arr: List) -> None:  # noqa
    """
    Find balanced parenthesis

    :param opn:
    :type opn:
    :param close:
    :type close:
    :param output:
    :type output:
    :param arr:
    :type arr:
    :return:
    :rtype:
    """
    if (opn == 0) and (close == 0):
        arr.append(output)
        return

    # Keep iterating until open count become zero
    if opn != 0:
        output1 = output
        output1 += '('
        balanced_parenthesis(opn - 1, close, output1, arr)

    # If close count is greater that the open count
    if close > opn:
        output2 = output
        output2 += ')'
        balanced_parenthesis(opn, close - 1, output2, arr)


def balanced_parenthesis1(n: int) -> List:
    """
    Balanced parenthesis

    :param n:
    :type n:
    :return:
    :rtype:
    """

    def rec(index: int, diff: int, comb: List, combs: List) -> None:
        """Recursive Function"""
        if (diff < 0) or (diff > index):
            return
        elif index == 0:
            if diff == 0:
                combs.append(''.join(comb))
        else:
            comb.append('(')
            rec(index - 1, diff + 1, comb, combs)
            comb.pop()
            comb.append(')')
            rec(index - 1, diff - 1, comb, combs)
            comb.pop()

    combinations = []
    rec(2 * n, 0, [], combinations)
    return combinations


if __name__ == '__main__':
    arr = []
    balanced_parenthesis(3, 3, '', arr)
    print(arr)
    print(balanced_parenthesis1(3))
