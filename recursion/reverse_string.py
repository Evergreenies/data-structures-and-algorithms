"""
Print string in reverse order
"""


def reverse_string(string: str) -> str:
    """
    Print string in reverse order

    :param string:
    :type string:
    :return:
    :rtype:
    """
    if not string:
        return ''
    return reverse_string(string[1:]) + string[0]


if __name__ == '__main__':
    inp_string = 'hello'
    print(reverse_string(inp_string))
