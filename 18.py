import numpy as np
from scipy.ndimage import binary_fill_holes

def neighbors(point,grid):
  x,y,z = point
  nbs = []
  nbs.extend([(x-1,y,z),(x+1,y,z)])
  nbs.extend([(x,y-1,z),(x,y+1,z)])
  nbs.extend([(x,y,z-1),(x,y,z+1)])
  nbs = [grid[a][b][c] for a,b,c in nbs]
  return sum(nbs)

f = open("inputs/18.txt")
data = f.read().split('\n')

PART2 = True
SIZE = 24
grid = np.zeros((SIZE,SIZE,SIZE)) # to inlude "-1" and "23"
newgrid = np.zeros((SIZE,SIZE,SIZE))

for line in data:
  x,y,z = map(int, line.split(','))
  grid[x+1][y+1][z+1] = 1

if PART2:
  grid = binary_fill_holes(grid)

total = 0
for line in data:
  x,y,z = map(int, line.split(','))
  newgrid[x+1][y+1][z+1] = 6 - neighbors((x+1,y+1,z+1),grid)

print(np.sum(newgrid))