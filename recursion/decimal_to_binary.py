"""
Program to conversion of Decimal Number to the Binary Form
"""


def decimal_to_binary(num: int, binary: str = '') -> str:
    """
    Decimal to Binary conversion

    :param num:
    :type num:
    :param binary:
    :type binary:
    :return:
    :rtype:
    """

    if num == 0:
        return binary

    division, reminder = divmod(num, 2)
    binary += str(reminder)
    return decimal_to_binary(division, binary)


if __name__ == '__main__':
    print(decimal_to_binary(233))
    print(decimal_to_binary(255))
