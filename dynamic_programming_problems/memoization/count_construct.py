"""
Write a function `count_construct(target, word_bank)` that accepts `target` as string
and `word_bank` as an array of string.

The function should return the number that represents the total ways number of ways
though target string can be constructed.

You may reuse elements of `word_bank` as many times as needed.
"""
from typing import List, Dict


def count_construct(target: str, arr: List, memoize: Dict) -> int:
    """
    Function that counts the number of ways to achieve target string.

    :param target:
    :type target:
    :param arr:
    :type arr:
    :param memoize:
    :type memoize:
    :return:
    :rtype:
    """
    if target in memoize:
        return memoize[target]

    if target == '':
        return 1

    count = 0
    for word in arr:
        if target.startswith(word):
            count += count_construct(target[len(word):], arr, memoize)

    memoize[target] = count
    return memoize[target]


if __name__ == '__main__':
    print(count_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl'], {}))
    print(count_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'], {}))
    print(count_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'], {}))
    print(count_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'], {}))
    print(count_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
        'e',
        'ee',
        'eee',
        'eeee',
        'eeeee',
        'eeeeee',
    ], {}))
