"""
We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in every subsequent row,
we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.

Table:-
n |k=1 2 3 4 5 6 7 8
1    0
2    0 1
3    0 1 1 0
4    0 1 1 0 1 0 0 1

Example 1:
Input: n = 1, k = 1
Output: 0

Example 2:
Input: n = 2, k = 1
Output: 0

Example 3:
Input: n = 2, k = 2
Output: 1
"""


def kth_symbol(n: int, k: int) -> int:
    """
    Find kth symbol in given grammar

    :param n:
    :type n:
    :param k:
    :type k:
    :return:
    :rtype:
    """
    # Return zero if n == k == 1
    if (n == 1) and (k == 1):
        return 0

    mid = (2 ** (n - 1)) // 2
    # If k <= mid then we have to look into the previous row i.e. (n - 1)
    if k <= mid:
        return int(kth_symbol(n - 1, k))
    else:
        # We are making inverse decisions due to the right from middle elements are exactly
        # inverse as compared to the left. So, again look into previous row with negation
        return int(not kth_symbol(n - 1, k - mid))


if __name__ == '__main__':
    assert kth_symbol(1, 1) == 0
    assert kth_symbol(2, 1) == 0
    assert kth_symbol(2, 2) == 1
    assert kth_symbol(4, 3) == 1
