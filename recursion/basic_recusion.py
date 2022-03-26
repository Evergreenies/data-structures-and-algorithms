"""
Simple recursion example
"""


def recursion_series(start: int, target: int, steps: int = 1):
    """Recursive function to print series"""

    if target < start:
        return 0

    print(start)

    return recursion_series(start + steps, target, steps)


if __name__ == '__main__':
    recursion_series(2, 100, steps=2)
