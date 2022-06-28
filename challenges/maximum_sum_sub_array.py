"""
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Complexity - O(n^2)
"""
import math


def brute_force_max_sum_subarray(arr: list) -> int | None:
    """
    Brute Force technique to find maximum sum of given subarray.

    :param arr: list of elements
    :type arr: list
    :return: max sum of subarray
    :rtype: int
    """
    if (not arr) or (len(arr) == 0):
        return None

    max_sum = arr[0]
    for index in range(len(arr)):
        j_idx = index
        current_sum = 0

        while j_idx < len(arr):
            current_sum += arr[j_idx]
            if current_sum > max_sum:
                max_sum = current_sum
            j_idx += 1

    return max_sum


"""
Efficient Approach: Kadane’s Algorithm

Kadane’s Algorithm is an iterative dynamic programming algorithm. It calculates the maximum sum subarray 
ending at a particular position by using the maximum sum subarray ending at the previous position. 
Follow the below steps to solve the problem.

Define two-variable currSum which stores maximum sum ending here and maxSum which stores maximum sum so far.
Initialize currSum with 0 and maxSum with INT_MIN.
Now, iterate over the array and add the value of the current element to currSum and check
If currSum is greater than maxSum, update maxSum equals to currSum.
If currSum is less than zero, make currSum equal to zero.
Finally, print the value of maxSum.

Complexity - O(n)
"""


def kadane_max_sum_subarray(arr: list) -> int | None:
    """
    Kadane's Algo to find maximum sum subarray of given array

    :param arr: list of elements
    :type arr: list
    :return: maximum sum subarray
    :rtype: int
    """
    if (not arr) or (len(arr) == 0):
        return None

    max_sum, current_sum = arr[0], 0
    for index in range(len(arr)):
        current_sum += arr[index]

        max_sum = max(current_sum, max_sum)
        current_sum = max(current_sum, 0)

    return max_sum


def max_sum_subarray_dynamic_programming(arr: list) -> int:
    """
    Solution to the maximum sum subarray by Dynamic Programming.

    :param arr:
    :type arr:
    :return:
    :rtype:
    """
    array = [0 for _ in range(len(arr) + 1)]
    array[0] = -math.inf

    for index in range(1, len(array)):
        array[index] = max(array[index - 1] + arr[index - 1], arr[index - 1])

    max_sum = array[0]
    for index in range(1, len(array)):
        if max_sum < array[index]:
            max_sum = array[index]

    return max_sum


if __name__ == '__main__':
    assert brute_force_max_sum_subarray([-3, -4, 5, -1, 2, -4, 6, -1]) == 8
    assert brute_force_max_sum_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert brute_force_max_sum_subarray([1]) == 1
    assert brute_force_max_sum_subarray([5, 4, -1, 7, 8]) == 23
    assert brute_force_max_sum_subarray([-1, -2, -3]) == -1

    assert kadane_max_sum_subarray([-3, -4, 5, -1, 2, -4, 6, -1]) == 8
    assert kadane_max_sum_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert kadane_max_sum_subarray([1]) == 1
    assert kadane_max_sum_subarray([5, 4, -1, 7, 8]) == 23
    assert kadane_max_sum_subarray([-1, -2, -3]) == -1

    assert max_sum_subarray_dynamic_programming([-3, -4, 5, -1, 2, -4, 6, -1]) == 8
    assert max_sum_subarray_dynamic_programming([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_sum_subarray_dynamic_programming([1]) == 1
    assert max_sum_subarray_dynamic_programming([5, 4, -1, 7, 8]) == 23
    assert max_sum_subarray_dynamic_programming([-1, -2, -3]) == -1
