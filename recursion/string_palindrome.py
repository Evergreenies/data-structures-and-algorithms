"""
Palindrome string using recursion
"""


def palindrome(string: str) -> bool:
    """
    Function to print string in reverse order

    :param string:
    :type string:
    :return:
    :rtype:
    """
    if (len(string) == 0) or (len(string) == 1):
        return True

    if string[0] == string[-1]:
        return palindrome(string[1:-1])
    return False


if __name__ == '__main__':
    assert palindrome('kayak') is True
    assert palindrome('kayyak') is True
    assert palindrome('string') is False
