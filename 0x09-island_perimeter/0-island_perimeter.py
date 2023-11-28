#!/usr/bin/python3
"""
0. Island Perimeter
"""


def island_perimeter(grid):
    """
    A function that returns the perimeter of the island described in grid

    Args:
        - grid (List): A two dimensional array representing a grid

    Return:
        Perimeter (int) of island
    """
    perimeter = 0
    islandCells = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                islandCells.append((i, j))

    for cell in islandCells:
        top = (cell[0] - 1, cell[1])
        down = (cell[0] + 1, cell[1])
        left = (cell[0], cell[1] - 1)
        right = (cell[0], cell[1] + 1)

        sides = 4
        for side in [top, down, left, right]:
            if side in islandCells:
                sides -= 1

        # if sides != 4:
        perimeter += sides

    return perimeter
    