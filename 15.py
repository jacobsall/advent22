from tqdm import tqdm

def manhattan(a, b):
    x1,y1 = a
    x2,y2 = b
    return abs(x1-x2)+abs(y1-y2)

f = open("inputs/15.txt")
data = f.read().split('\n')
sublines = [[subline for subline in line.split(':')] for line in data]

PART1 = False
sensors = []
dists = []
beacons = set()

for subline in sublines:
  s = subline[0].split(',')
  sx = int(s[0].split('=')[1])
  sy = int(s[1].split('=')[1])
  sensor = (sx,sy)
  
  b = subline[1].split(',')
  bx = int(b[0].split('=')[1])
  by = int(b[1].split('=')[1])
  beacon = (bx,by)

  sensors.append(sensor)
  dists.append(manhattan(sensor,beacon))
  beacons.add(beacon)

things = list(zip(sensors,dists))

bxs = [x for x,_ in beacons]
xmin = min(bxs)
xmax = max(bxs)

print(xmin,xmax)
impossible = set()


if PART1:
  y = 2000000
  for x in tqdm(range(xmin*2,xmax*2)):
    point = (x,y)
    for sensor,dist in things:
      if manhattan(sensor,point) <= dist:
        if point not in beacons and point not in sensors:
          impossible.add(point)

  print(len(impossible))

# if False:
#   thing = list(zip(*list(impossible)))
#   sensors = list(zip(*list(set(sensors))))
#   beacons = list(zip(*list(set(beacons))))
#   ax = plt.figure().gca()
#   ax.invert_yaxis()
#   ax.yaxis.set_major_locator(MaxNLocator(integer=True))
#   ax.xaxis.set_major_locator(MaxNLocator(integer=True))
#   ax.scatter(thing[0],thing[1])
#   ax.scatter(sensors[0],sensors[1],c='r')
#   ax.scatter(beacons[0],beacons[1],c='g')
#   ax.grid(True)
#   plt.show()