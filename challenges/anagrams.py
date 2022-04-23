"""
Given two strings S1 and S2, check if they are anagrams. Two strings are anagrams if
they are made the same character with the same frequencies.
"""


def anagram(string1: str, string2: str) -> bool:
    """
    Function to find string anagram.

    :param string1:
    :type string1:
    :param string2:
    :type string2:
    :return:
    :rtype:
    """
    string1, string2 = string1.lower(), string2.lower()

    counter = dict()
    for char in string1:
        if counter.get(char) is None:
            counter[char] = 0
        counter[char] += 1

    for char in string2:
        if counter.get(char) is None:
            return False

        counter[char] -= 1
        if counter[char] < 0:
            return False

    return True


if __name__ == '__main__':
    print(anagram('nature', 'future'))
    print(anagram('anagram', 'nagaram'))
    print(anagram('abc', 'cba'))
    print(anagram('nameless', 'salesman'))
