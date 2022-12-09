import numpy as np

def myHash(npList):
  return str(npList[0]) + str(npList[1])

f = open("inputs/9.txt")
data = f.read().split('\n')

TAILS = 9
SIZE = (21,26)
DRAW = False

s = np.array([10000,10000])
tails = [s.copy() for _ in range(0,TAILS+1)]

positions = set()
positions.add(myHash(tails[-1]))

moves = [[line.split(' ')[0],int(line.split(' ')[1])] for line in data]

def dirToCoord(d):
  if d == 'U':
    return np.array([0,1])
  elif d == 'D':
    return np.array([0,-1])
  elif d == 'L':
    return np.array([-1,0])
  elif d == 'R':
    return np.array([1,0])
  else:
    return np.array([0,0])

def isAdjacent(H,T):
  return np.linalg.norm(H - T) <= np.sqrt(2)

def getTail(H,T):
  # print(H,T)
  if isAdjacent(H,T): return dirToCoord("Stay")
  # something broken with negative, start at large x to work lol :)))
  a = 0 if H[0] == T[0] else (1 if H[0] > T[0] else -1)
  b = 0 if H[1] == T[1] else (1 if H[1] > T[1] else -1)
  
  return np.array([a,b])

def drawBoard(items,origin=s,size=SIZE):

  a = np.full(size,'.')

  a[len(a)-1-s[1]][s[0]] = 's'

  for idx,item in reversed(list(enumerate(items))):
    y,x = item
    a[len(a)-1-x][y] = str(idx)
    # print(x,y)

  for line in a:
    print (''.join(map(str, line)))
  print('----------------------------------------------------------------------------')

for move in moves:
  for step in range(0,move[1]):
    tails[0] += dirToCoord(move[0])

    prev = tails[0]
    for tail in tails[1:]:
      tail += getTail(prev,tail)
      prev = tail

    positions.add(myHash(prev))
  if DRAW: drawBoard(items = tails,origin=s)
print(len(positions))