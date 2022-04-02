"""
Print N-Bits binary numbers having more 1's than 0's for any prefix
Ex -
INPUT:
    N = 3

OUTPUT:
    111
    110
    101
"""


def find_n_binary_digits(ones: int, zeros: int, n: int, op: str) -> None:
    """
    Finding all binary number which has number of one's greater than zero's

    :param ones:
    :type ones:
    :param zeros:
    :type zeros:
    :param n:
    :type n:
    :param op:
    :type op:
    :return:
    :rtype:
    """
    if n == 0:
        print(op)
        return

    op1 = op
    op1 += '1'
    find_n_binary_digits(ones + 1, zeros, n - 1, op1)

    # Check whether we can add zeros or not
    if ones > zeros:
        op2 = op
        op2 += '0'
        find_n_binary_digits(ones, zeros + 1, n - 1, op2)


if __name__ == '__main__':
    find_n_binary_digits(0, 0, 3, '')
