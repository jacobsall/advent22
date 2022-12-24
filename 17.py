from itertools import cycle
from tqdm import tqdm
from collections import deque
import copy

class Shape:
  def __init__(self, origin, shape=0):
    self.points = set()
    self.falling = False
    match shape:
      case 0:
        self.points.add(origin)
        self.points.add((origin[0]-1,origin[1]))
        self.points.add((origin[0]+1,origin[1]))
        self.points.add((origin[0]+2,origin[1]))
      case 1:
        self.points.add(origin)
        self.points.add((origin[0],origin[1]+1))
        self.points.add((origin[0],origin[1]+2))
        self.points.add((origin[0]-1,origin[1]+1))
        self.points.add((origin[0]+1,origin[1]+1))
      case 2:
        self.points.add(origin)
        self.points.add((origin[0]-1,origin[1]))
        self.points.add((origin[0]+1,origin[1]))
        self.points.add((origin[0]+1,origin[1]+1))
        self.points.add((origin[0]+1,origin[1]+2))
      case 3:
        self.points.add((origin[0]-1,origin[1]))
        self.points.add((origin[0]-1,origin[1]+1))
        self.points.add((origin[0]-1,origin[1]+2))
        self.points.add((origin[0]-1,origin[1]+3))
      case 4:
        self.points.add(origin)
        self.points.add((origin[0],origin[1]+1))
        self.points.add((origin[0]-1,origin[1]))
        self.points.add((origin[0]-1,origin[1]+1))
      case other:
        raise Exception("wth, no such shape")

  def intersect(self, points1: set, points2: set):
    # print('1')
    if any([p[0] <= 0 or p[0] >= 8 for p in points1]): return True
    # print('2')
    if any([p[1] == 0 for p in points1]): return True
    # print('3')
    return points2.intersection(points1)

  def fall(self):
    self.falling = False
    new_points = set([(p[0],p[1]-1)for p in self.points])
    return new_points

  def shift(self,direction):
    self.falling = True
    i = -1 if direction == '<' else 1
    new_points = set([(p[0]+i,p[1])for p in self.points])
    return new_points

  def moveTo(self,points):
    self.points = points

f = open("inputs/17.txt")
data = f.read()
gas = cycle([char for char in data])
shapes = cycle([0,1,2,3,4])

# previous = deque(maxlen=20)

AMOUNT = 2022
height = 0
points = set()
for i in tqdm(range(0,AMOUNT)):
  rock = Shape((4,height+4),next(shapes))
  new_points = copy.deepcopy(rock.points)

  while True:
    new_points = rock.shift(next(gas))
    if not rock.intersect(new_points,points):
      rock.moveTo(new_points)

    new_points = rock.fall()
    if rock.intersect(new_points,points):
      break

    rock.moveTo(new_points)

  points.update(rock.points)
  height = max([p[1] for p in rock.points]+[height])

print(height)