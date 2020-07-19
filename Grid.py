__author__ = "Petar Ulev"

import numpy as np


# Green vs red
# Green - 1
# Red - 0
class Grid:
    def __init__(self, grid):
        # Generation Zero
        self.grid = grid
        self.x = self.grid.shape[1]  # number of columns
        self.y = self.grid.shape[0]  # number of rows
        assert self.is_valid_grid()

    def is_valid_grid(self):
        # Ensure assumption about x and y holds.
        return 1000 > self.y >= self.x

    def create_generation(self):
        # Create next generation
        for i in range(0, self.y):  # Iterate over rows
            for j in range(0, self.x):  # Iterate over columns
                neighbours = []
                # Check all surrounding cells (neighbours) of current cell,
                # making sure no exception is thrown if some neighbour
                # does not exist (if cell is on a corner or a side).
                if i - 1 >= 0:  # Index check
                    neighbours.append(self.grid[i - 1, j].get_color())  # Push neighbour to array
                if i - 1 >= 0 and j + 1 < self.x:
                    neighbours.append(self.grid[i - 1, j + 1].get_color())
                if j + 1 < self.x:
                    neighbours.append(self.grid[i, j + 1].get_color())
                if i + 1 < self.y and j + 1 < self.x:
                    neighbours.append(self.grid[i + 1, j + 1].get_color())
                if i + 1 < self.y:
                    neighbours.append(self.grid[i + 1, j].get_color())
                if j - 1 >= 0 and i + 1 < self.y:
                    neighbours.append(self.grid[i + 1, j - 1].get_color())
                if j - 1 >= 0:
                    neighbours.append(self.grid[i, j - 1].get_color())
                if j - 1 >= 0 and i - 1 >= 0:
                    neighbours.append(self.grid[i - 1, j - 1].get_color())

                green_neighbours = 0
                red_neighbours = 0

                for neighbour in neighbours:  # Find how many green and red neighbours current cell has.
                    if neighbour == 1:
                        green_neighbours += 1
                    if neighbour == 0:
                        red_neighbours += 1
                if self.grid[i, j].get_color() == 0:  # if the cell is red, check for conditions 1 and 2
                    if green_neighbours == 3 or green_neighbours == 6:  # Condition 1
                        self.grid[i, j].set_next_color(1)  # Change to green
                    # Condition 2 needs no more programming.
                elif self.grid[i, j].get_color() == 1:  # if the cell is green, check for conditions 3 and 4
                    if not (green_neighbours == 2 or green_neighbours == 3 or green_neighbours == 6):  # Condition 3
                        self.grid[i, j].set_next_color(0)  # Change to red
                    # Condition 4 needs no more programming
        self.color_grid() # Colors the grid with the next colors

    def color_grid(self):
        # Colors every cell if it has non-None next color.
        for i in range(0, self.y):  # Iterate over rows
            for j in range(0, self.x):  # Iterate over columns
                cell = self.grid[i, j]
                cell.color_cell()

    def compute(self, x, y, N):
        # Computes the number of generations in which cell (x, y)
        # was green (from gen. Zero to gen N, including).
        answer = 0
        if self.grid[x, y].get_color() == 1:  # If the cell was green initally.
            answer = 1
        for i in range(0, N):
            self.create_generation()
            if self.grid[x, y].get_color() == 1:
                answer += 1
        return answer
