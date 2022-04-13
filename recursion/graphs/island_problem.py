"""
Island Count

Write a program to count gid containing W's and L's. Where W represents Water and L represents Land.
The function should return the number of island on the grid. An island is vertically or horizontally
connected region of land.
"""
from typing import List, Set


def island_count(grid: List) -> int:
    """
    Island count

    :param grid:
    :type grid:
    :return:
    :rtype:
    """
    visited, count = set(), 0
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if explore(grid, row, column, visited) is True:
                count += 1
    return count


def explore(grid: List, row: int, column: int, visited: Set) -> bool:
    """
    Explore path or neighbour's of current positional element

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
    row_bounds = (0 <= row) and (row < len(grid))
    column_bound = (0 <= column) and (column < len(grid[0]))

    # Checkin whether recursion inside in the grid
    if (not row_bounds) or (not column_bound):
        return False

    # Skip execution if current node is water
    if grid[row][column] == 'W':
        return False

    position = f'{row},{column}'
    if position in visited:
        return False
    visited.add(position)

    # Search neighbour elements of current element
    explore(grid, row - 1, column, visited)
    explore(grid, row + 1, column, visited)
    explore(grid, row, column - 1, visited)
    explore(grid, row, column + 1, visited)

    return True


if __name__ == '__main__':
    grd = [
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'L', 'W'],
        ['W', 'W', 'L', 'L', 'W'],
        ['L', 'W', 'W', 'L', 'L'],
        ['L', 'L', 'W', 'W', 'W'],
    ]
    print(island_count(grd))
