
in_data = open('data/grid_20.txt', 'r').read()

# Construct list of lists
in_data = in_data.split('\n')
grid = list()
for row in range(0, 20):
    grid.append(in_data[row].split(' '))

# Convert all strings to ints
for row in range(0, 20):
    for col in range(0, 20):
        grid[row][col] = int(grid[row][col])

# Check the combos
max_prod = 0
for row in range(0, 20):
    for col in range(0, 20):
        # Left to right
        if col < 17:
            max_prod = max(max_prod, grid[row][col] * grid[row][col+1] * grid[row][col+2] * grid[row][col+3])

            # Diagonal
            if row < 17:
                max_prod = max(max_prod, grid[row][col] * grid[row+1][col+1] * grid[row+2][row+2] * grid[row+3][col+3])

        # Top to bottom
        if row < 17:
            max_prod = max(max_prod, grid[row][col] * grid[row+1][col] * grid[row+2][col] * grid[row+3][col])

print(max_prod)
print(grid)
