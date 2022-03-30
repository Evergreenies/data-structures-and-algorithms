"""
Calculate power of given number
"""


def power_calculator(base: int | float, exponent: int | float) -> float | None | int:
    """
    Calculating power of given number

    :param base:
    :type base:
    :param exponent:
    :type exponent:
    :return:
    :rtype:
    """
    if exponent < 0:
        return

    if exponent == 0:
        return 1

    return base * power_calculator(base, exponent - 1)


if __name__ == '__main__':
    assert power_calculator(3, 3) == 27
    assert power_calculator(5, 2) == 25
