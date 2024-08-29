#!/usr/bin/python3
"""
This module contains a function to calculate the perimeter of an island.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid.

    Args:
    grid (List[List[int]]): A list of list of integers where:
        - 0 represents water
        - 1 represents land

    Returns:
    int: The perimeter of the island.

    Note:
    - Each cell is square, with a side length of 1
    - Cells are connected horizontally/vertically (not diagonally).
    - The grid is rectangular, width and height don't exceed 100
    - The grid is completely surrounded by water
    - There is only one island (or nothing).
    - The island doesn't have "lakes"
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2

    return perimeter
