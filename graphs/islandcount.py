grid = [
  ['L', 'W', 'W', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['W', 'L', 'W', 'L', 'W'],
  ['W', 'W', 'W', 'W', 'W'],
  ['W', 'W', 'L', 'L', 'L'],
];



def count_islands(grid:list):
    number_of_islands = 0
    visited = set()
    for i,row in enumerate(grid):
        for j,col in enumerate(row):
            if explore(grid,i,j,visited):
                number_of_islands += 1
    return number_of_islands

def explore(grid,row,col,visited):
    pos = str(row) + "," + str(col)
    if pos in visited:
        return False
    visited.add(pos)
    row_check = row >= 0 and row < len(grid)
    col_check = col >= 0 and col < len(grid[0])
    if not row_check or not col_check:
        return False
    if grid[row][col] == 'W':
        return False
    explore(grid,row-1,col,visited)
    explore(grid,row,col+1,visited)
    explore(grid,row+1,col,visited)
    explore(grid,row,col-1,visited)
    return True

print(count_islands(grid))