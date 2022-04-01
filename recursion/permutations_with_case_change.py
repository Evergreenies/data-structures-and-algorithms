"""
Printing permutations with case changing
"""


def permutations(ip: str, op: str) -> None:
    """
    Printing permutations with case changing

    :param ip:
    :type ip:
    :param op:
    :type op:
    :return:
    :rtype:
    """
    if len(ip) == 0:
        print(op)
        return

    op1, op2 = op, op
    op1 = op1 + ip[0]
    op2 = op2 + ip[0].upper()
    ip = ip[1:]

    permutations(ip, op1)
    permutations(ip, op2)


if __name__ == '__main__':
    permutations('abc', '')
