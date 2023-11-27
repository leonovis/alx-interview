#!/usr/bin/python3
"""Island Perimeter
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island
    Args:
        grid: list of integers 0 represnts water and 1 represents land
        rectangular in shape ahving width and height <100
    Return:
        the perimeter of the island described in a grid
    """

    pr = 0
    for a in range(len(grid)):
        for b in range(len(grid[a])):
            if (grid[a][b] == 1):
                if (a <= 0 or grid[a - 1][b] == 0):
                    pr += 1
                if (a >= len(grid) - 1 or grid[a + 1][b] == 0):
                    pr += 1
                if (b <= 0 or grid[a][b - 1] == 0):
                    pr += 1
                if (a >= len(grid[a]) - 1 or grid[a][b + 1] == 0):
                    pr += 1
    return pr
