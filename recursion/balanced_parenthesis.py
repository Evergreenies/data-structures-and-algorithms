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


if __name__ == '__main__':
    arr = []
    balanced_parenthesis(3, 3, '', arr)
    print(arr)
