__author__ = "Petar Ulev"

from Grid import Grid
import numpy as np
from Cell import Cell
# Factory class for creating a grid and storing problem-related variables.
class GridFactory:
    def __init__(self, x, y, grid, N):
        # x, y - grid dimensions
        # grid - 2d numpy array of zeroes and ones
        # x1, y1 - coordinates of cell of interest
        # N - number of generations, including generation Zero and generation N
        self.x = x
        self.y = y
        self.grid = Grid(self.create_grid(grid))
        self.N = N

    def get_grid(self):  # Getter.
        return self.grid

    def create_grid(self, grid):
        for i in range(0, self.y):
            for j in range(0, self.x):
                grid[i][j] = Cell(grid[i][j])
        return np.array(grid)



