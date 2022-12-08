f = open("inputs/8.txt")
data = f.read().split('\n')

grid = [[int(char) for char in line] for line in data]


def checkRow(row,idx,tree):
  if idx == 0 or idx == len(row)-1: return True
  if all(i < tree for i in row[0:idx]) or all(i < tree for i in row[idx+1:len(row)]):
    return True
  return False

def rowScore(row,idx,tree):
  if idx == 0 or idx == len(row)-1: return 0

  before = 0
  for i in reversed(row[0:idx]):
    before += 1
    if i >= tree: break
    
  after = 0
  for i in row[idx+1:len(row)]:
    after += 1
    if i >= tree: break
  return before * after

total = 0
maximum = -1

for r_idx,row in enumerate(grid):
  for c_idx,tree in enumerate(row):
    col = [r[c_idx] for r in grid]
    result = checkRow(row,c_idx,tree) or checkRow(col,r_idx,tree) 
    score = rowScore(row,c_idx,tree) * rowScore(col,r_idx,tree)
    
    total += 1 if result else 0
    maximum = score if maximum < score else maximum

print("part 1: ",total)
print("part 2: ",maximum)
