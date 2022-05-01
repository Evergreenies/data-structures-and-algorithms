"""
Write a function `all_construct(target, word_bank)` which can accepts target as string and
word_bank as arr of strings.

The function should return a 2D array containing *all the ways* that the `target` can be
constructed by containing elements of the array `word_bank`. Each element of 2D array
should represent one combination that constructs the `target`.

You may reuse elements of `word_bank` as many times as needed.
"""
from typing import List, Dict


def all_construct(target: str, word_bank: List, memoize: Dict) -> List:
    if target in memoize:
        return memoize[target]

    if target == '':
        return [[]]

    result = []
    for word in word_bank:
        if target.startswith(word):
            suffix_ways = all_construct(target[len(word):], word_bank, memoize)
            target_ways = map(lambda sub_list: [word, *sub_list], suffix_ways)  # noqa
            result.extend(target_ways)

    memoize[target] = result
    return result


if __name__ == '__main__':
    print(all_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl'], {}))
    print(all_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'], {}))
    print(all_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'], {}))
    print(all_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'], {}))
    print(all_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
        'e',
        'ee',
        'eee',
        'eeee',
        'eeeee',
        'eeeeee',
    ], {}))
