"""
Print Subsets
Print Power Sets
Print all subsequences
"""


def subsets(ip: str, op: str) -> None:  # noqa
    """
    Print subsets

    :param ip:
    :type ip:
    :param op:
    :type op:
    :return:
    :rtype:
    """
    if len(ip) == 0:
        print("==> ", op)
        return

    op1, op2 = op, op
    op1 = op1 + ip[0]  # noqa
    ip = ip[1:]  # noqa
    subsets(ip, op1)
    subsets(ip, op2)


if __name__ == '__main__':
    ip = 'ab'
    op = ''
    subsets(ip, op)
