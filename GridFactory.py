__author__ = "Petar Ulev"

from Grid import Grid
import numpy as np

# Factory class for creating a grid and storing problem-related variables.
class GridFactory:
    def __init__(self, x, y, grid, N):
        # x, y - grid dimensions
        # grid - 2d numpy array of zeroes and ones
        # x1, y1 - coordinates of cell of interest
        # N - number of generations, including generation Zero and generation N
        self.x = x
        self.y = y
        self.grid = Grid(np.array(grid))
        self.N = N

    def get_grid(self):  # Getter.
        return self.grid
