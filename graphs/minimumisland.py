grid = [
  ['L', 'W', 'W', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['W', 'L', 'W', 'L', 'W'],
  ['W', 'W', 'W', 'W', 'W'],
  ['W', 'W', 'L', 'L', 'L'],
]



def count_islands(grid:list):
    number_of_islands = 0
    visited = set()
    min_size = float('inf')
    for i,row in enumerate(grid):
        for j,col in enumerate(row):
            size = explore(grid,i,j,visited)
            if size > 0 and size < min_size:
                min_size = size
    return min_size

def explore(grid,row,col,visited):
    pos = str(row) + "," + str(col)
    if pos in visited:
        return 0
    visited.add(pos)
    row_check = row >= 0 and row < len(grid)
    col_check = col >= 0 and col < len(grid[0])
    if not row_check or not col_check:
        return 0
    if grid[row][col] == 'W':
        return 0
    size = 1
    size+=explore(grid,row-1,col,visited)
    size+=explore(grid,row,col+1,visited)
    size+=explore(grid,row+1,col,visited)
    size+=explore(grid,row,col-1,visited)
    return size

print(count_islands(grid))