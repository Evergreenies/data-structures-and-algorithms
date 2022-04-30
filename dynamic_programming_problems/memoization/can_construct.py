"""
Write a function `can_construct(string, word_bank)` that accepts string and string of array.

The function should return indicating whether the `target` can be constructed by concatenating
elements of the word `word_bank` array.

You may use elements of `word_bank` as many times as you needed.
"""
from typing import List, Dict


def can_construct(target: str, arr: List, memoize: Dict) -> bool:
    """
    Construct a string by provided array of words.

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
        return True

    for word in arr:
        if target.startswith(word) and (can_construct(target[len(word):], arr, memoize) is True):
            memoize[target] = True
            return memoize[target]

    memoize[target] = False
    return False


if __name__ == '__main__':
    print(can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'], {}))
    print(can_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'], {}))
    print(can_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'], {}))
    print(can_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
        'e',
        'ee',
        'eee',
        'eeee',
        'eeeee',
        'eeeeee',
    ], {}))
