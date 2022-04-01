"""
Print permutations with spaces
"""


def permutations(ip: str, op: str) -> None:
    """
    Permutations with spaces

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

    op1 = op
    op2 = op

    op1 = op1 + ('_' if op1 else '')
    op1 = op1 + ip[0]
    op2 = op2 + ip[0]
    ip = ip[1:]

    permutations(ip, op1)
    permutations(ip, op2)


if __name__ == '__main__':
    permutations('ABC', '')
