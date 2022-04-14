import math
from typing import List, Set


def smallest_island(grid: List) -> int:
    """
    Finding smallest island in given grid

    :param grid:
    :type grid:
    :return:
    :rtype:
    """
    smallest, visited = math.inf, set()

    for row in range(len(grid)):
        for column in range(len(grid[0])):
            size = explore(grid, row, column, visited)
            if (size > 0) and (size < smallest):
                smallest = size
    return smallest


def explore(grid: List, row: int, column: int, visited: Set) -> int:
    """
    Exploring neighbours of current positional element

    :param grid:
    :type grid:
    :param row:
    :type row:
    :param column:
    :type column:
    :param visited:
    :type visited:
    :return:
    :rtype:
    """
    # Check whether lookup in inside grid given
    row_bounds = (0 <= row) and (row < len(grid))
    column_bounds = (0 <= column) and (column < len(grid[0]))
    if (not row_bounds) or (not column_bounds):
        return 0

    # Skip if current node is water
    if grid[row][column] == 'W':
        return 0

    position = f'{row},{column}'
    if position in visited:
        return 0
    visited.add(position)

    small = 1
    small += explore(grid, row - 1, column, visited)
    small += explore(grid, row + 1, column, visited)
    small += explore(grid, row, column - 1, visited)
    small += explore(grid, row, column + 1, visited)
    return small


if __name__ == '__main__':
    grd = [
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'L', 'W'],
        ['W', 'W', 'L', 'L', 'W'],
        ['L', 'W', 'W', 'L', 'L'],
        ['L', 'L', 'W', 'W', 'W'],
    ]
    print(smallest_island(grd))
