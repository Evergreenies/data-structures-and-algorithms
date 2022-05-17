"""
Given an array of n integers where each value represents the number of chocolates in a packet.
Each packet can have a variable number of chocolates. There are m students, the task is to
distribute chocolate packets such that:

Each student gets one packet.
The difference between the number of chocolates in the packet with maximum chocolates and packet
with minimum chocolates given to the students is minimum.
"""


def find_min_diff(arr: list, size: int) -> int:
    """
    Chocolate distribution

    :param arr:
    :type arr:
    :param size:
    :type size:
    :return:
    :rtype:
    """
    length = len(arr)

    if (size == 0) or (length == 0):
        return 0

    if length < size:
        return -1

    arr.sort()
    min_diff = arr[-1] - arr[0]
    for index in range(length - size + 1):
        min_diff = min(min_diff, (arr[index + size - 1] - arr[index]))
    return min_diff


if __name__ == '__main__':
    input_arr = [12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50]
    assert find_min_diff(input_arr, 7) == 10

    input_arr = []
    assert find_min_diff(input_arr, 5) == 0

    input_arr = [23]
    assert find_min_diff(input_arr, 1) == 0
