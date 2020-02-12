puzzle = [
  [8,5,0,0,0,0,0,0,0],
  [0,0,0,1,3,0,0,0,0],
  [4,0,0,0,0,0,0,9,0],
  [0,2,0,9,0,8,0,0,0],
  [5,8,1,0,0,0,0,0,0],
  [0,0,0,0,0,0,7,0,0],
  [0,0,7,0,0,1,8,0,0],
  [0,0,0,0,8,0,9,0,0],
  [0,0,0,0,0,0,2,1,0]
]

def solve():
  global puzzle
  
  for i in range(len(puzzle)):
    for j in range(len(puzzle[i])):
      if(puzzle[i][j] == 0):
        for n in range(1, 10):
          if(canPlace(j, i, n)): 
            puzzle[i][j] = n
            solve()
            puzzle[i][j] = 0
        return
  for line in puzzle:
    print(line)
  input("next solution")
  

def canPlace(x, y, n):
  global puzzle
  for i in range(0, 9):
    if(puzzle[y][i] == n): return False;
    if(puzzle[i][x] == n): return False;
  
  x = x // 3
  y = y // 3
  
  for i in range(x * 3, x * 3 + 3):
    for j in range(y * 3, y * 3 + 3):
      if(puzzle[y][x] == n): return False;
  return True

solve()
