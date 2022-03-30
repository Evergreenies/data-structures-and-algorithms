"""
Triangular Number

Calculates the nth triangular number.

A triangular number counts the objects that can form an equilateral triangle.
The nth triangular number is the number of dots composing a triangle with n dots on a side,
and is equal to the sum of the n natural numbers from 1 to n.

This is the Triangular Number Sequence: 1, 3, 6, 10, 15, 21, 28, 36, 45
                          *
            *           *    *
*     |   *   *  |   *    *    *  |

1st      2nd             3rd             nth?
1st triangular number   :   1
2nd = (1+2)             :   3
3rd = (1+2+3)           :   6
5th = (1+2+3+4+5)       :   15

Input: 5
Output: 15
"""


def triangular_number(num: int) -> int:
    """
    Find triangular number

    :param num:
    :type num:
    :return:
    :rtype:
    """
    if num < 2:
        return num
    return num + triangular_number(num - 1)


def display_pyramids(num: int) -> int:
    """
    Printing pyramids

    :param num:
    :type num:
    :return:
    :rtype:
    """
    for i in range(1, num + 1):
        print(' ' * (num - i), '* ' * i)
    return num


if __name__ == '__main__':
    assert display_pyramids(triangular_number(5)) == 15
