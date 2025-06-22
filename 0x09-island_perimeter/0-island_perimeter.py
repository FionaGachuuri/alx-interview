#!/usr/bin/python3
"""
Function that calculates the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in the grid.
    """
    if not grid or not grid[0]:
        return 0

    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Start with 4 sides
                perimeter += 4

                # Check for neighboring land cell above
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # shared side with top cell

                # Check for neighboring land cell to the left
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # shared side with left cell

    return perimeter
