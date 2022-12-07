f = open("inputs/7.txt")
data = f.read().split('\n')

tree = {}
path = []

bigtotal = 0

def current_level(tree,path):
  level = tree
  for subpath in path:
    level = level[subpath]
  return level

for line in data:
  splitline = line.split(' ')
  if splitline[0] == '$' and splitline[1] == 'cd':
    if splitline[2] == '..':
      path.pop()
    elif splitline[2] in current_level(tree,path):
      path.append(splitline[2])
    else:
      current_level(tree,path)[splitline[2]] = {}
      path.append(splitline[2])
  elif splitline[0] == 'dir':
    current_level(tree,path)[splitline[1]] = {}
  elif splitline[0].isnumeric():
    current_level(tree,path)[splitline[1]+".file"] = int(splitline[0])


totals = {}
def traverse(tree, path):
  current = ' '.join(path)
  if current not in totals:
    totals[current] = 0

  children = current_level(tree,path)
  for child,value in children.items():
    if isinstance(value,int):
      totals[current] += value
    elif isinstance(value,dict):
      path.append(child)
      traverse(tree,path)
      totals[current] += totals[current+ " " + child]
      path.pop()

traverse(tree,['/'])

answer1 = sum([total for total in totals.values() if total <= 100000])
print(f"part 1: ", answer1)

disk_space = 70000000
left = disk_space - totals['/']
unused = 30000000
needed = unused - left

answer2 = sorted([total for total in totals.values() if total >= needed])[0]
print(f"part 2: ", answer2)
