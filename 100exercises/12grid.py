def numCells(grid):
    n = len(grid)
    m = len(grid[0])

    count = 0
    for i in range(n):
        for j in range(m):
            current_cell = grid[i][j]
            is_dominant = True

            for x in range(max(0, i - 1), min(n, i + 2)):
                for y in range(max(0, j - 1), min(m, j + 2)):
                    if not (x == i and y == j) and grid[x][y] >= current_cell:
                        is_dominant = False
                        break
                if not is_dominant:
                    break

            if is_dominant:
                count += 1

    return count

grid = [
    [1, 2, 7],
    [4, 5, 6],
    [8, 8, 9]
]

print(numCells(grid))