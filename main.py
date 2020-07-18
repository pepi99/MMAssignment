__author__ = "Petar Ulev"

from GridFactory import GridFactory

size = list(map(int, input().split(', ')))  # Get the size of the grid in array format

x = size[0]
y = size[1]
grid = []

for j in range(0, y):  # Add every row into the grid array
    row = list(map(int, list(input())))
    assert len(row) == x  # Check dimension
    grid.append(row)

coordinates_N = list(map(int, input().split(', ')))  # Get the cell of interest and N in array format
x1 = coordinates_N[0]
y1 = coordinates_N[1]
N = coordinates_N[2]

gf = GridFactory(x, y, grid, N)  # Make a grid factory
grid = gf.get_grid()  # Obtain the grid
answer = grid.compute(y1, x1, N)  # Actual computation
print(answer)  # Print result
