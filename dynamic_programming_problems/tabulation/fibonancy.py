"""
Write a function `fib(n)` that takes in number as argument.
The function should return the nth number of fibonancy sequence.
"""


def fib(n: int) -> int:
    """
    Fibonancy series

    :param n:
    :type n:
    :return:
    :rtype:
    """
    dp_table = [0 for _ in range(n + 2)]
    dp_table[1] = 1

    for ele in range(n):
        dp_table[ele + 1] += dp_table[ele]
        dp_table[ele + 2] += dp_table[ele]

    return dp_table[n]


if __name__ == '__main__':
    print(fib(6))
    print(fib(7))
    print(fib(8))
    print(fib(50))
