f = open("inputs/14.txt")
data = f.read().split('\n')
lines = [[[int(c) for c in coord.split(',')] for coord in line.split(' -> ')] for line in data]

def flatten(l):
  return [item for sublist in l for item in sublist]

PART2 = True

max_x = max([items[0] for items in flatten(lines)])
min_x = min([items[0] for items in flatten(lines)])
max_y = max([items[1] for items in flatten(lines)])


if PART2: 
  lines.append([[min_x-1000,max_y+2],[max_x+1000,max_y+2]])
  max_x = max([items[0] for items in flatten(lines)])
  min_x = min([items[0] for items in flatten(lines)])
  max_y = max([items[1] for items in flatten(lines)])



cols = max_x-min_x+1
rows = max_y+1

board = [['.']*(cols) for i in range(rows)]

for line in lines:
  for idx,coords in enumerate(line[:-1]):
    if coords[0] < line[idx+1][0]:
      for i in range(abs(coords[0]-line[idx+1][0])+1):
        board[coords[1]][coords[0]-min_x+i] = '#'
    elif coords[0] > line[idx+1][0]:
      for i in range(abs(coords[0]-line[idx+1][0])+1):
        board[coords[1]][coords[0]-min_x-i] = '#'
    elif coords[1] < line[idx+1][1]:
      for i in range(abs(coords[1]-line[idx+1][1])+1):
        board[coords[1]+i][coords[0]-min_x] = '#'
    elif coords[1] > line[idx+1][1]:
      for i in range(abs(coords[1]-line[idx+1][1])+1):
        board[coords[1]-i][coords[0]-min_x] = '#'


for line in board:
  if not PART2:
    print (''.join(map(str, line)))


running = True
sands = 0

curr = [500-min_x,0]
while running:
  if curr[1] == max_y:
    # running = False
    break
  if board[curr[1]+1][curr[0]] == '.':
    curr[1] += 1
  elif curr[0] == 0:
    # running = False
    break
  elif board[curr[1]+1][curr[0]-1] == '.':
    curr[1] += 1
    curr[0] -= 1
  elif curr[0] == max_x:
    # running = False
    break
  elif board[curr[1]+1][curr[0]+1] == '.':
    curr[1] += 1
    curr[0] += 1
  else:
    
    board[curr[1]][curr[0]] = 'o'
    sands += 1
    if curr == [500-min_x,0]:
      break
    curr = [500-min_x,0]


for line in board:
  if not PART2:
    print (''.join(map(str, line)))

print('sands: ',sands)