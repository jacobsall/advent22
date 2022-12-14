import ast
import itertools
from functools import cmp_to_key


f = open("inputs/13.txt")
data = f.read().split('\n\n')

def resolve(a,b):
  if isinstance(a,int) and isinstance(b,int):
    if a < b: return -1
    elif a > b: return 1
    else: return 0
  if isinstance(a,list) and isinstance(b,int):
    return resolve(a,[b])
  if isinstance(a,int) and isinstance(b,list):
    return resolve([a],b)
  if isinstance(a,list) and isinstance(b,list):
    for x,y in itertools.zip_longest(a,b):
      if x == None: return -1
      if y == None: return 1
      res = resolve(x,y)
      if res != 0: return res
    return 0

pairs = 0
packets = []
for idx,group in enumerate(data):
  lines = group.split('\n')
  line1 = ast.literal_eval(lines[0])#resolve(group[0])
  line2 = ast.literal_eval(lines[1])
  
  packets.extend([line1,line2])
  res = resolve(line1,line2)
  if res == -1: pairs += idx+1

print('part 1:',pairs)

packets.extend([[[2]],[[6]]])
packets = sorted(packets,key=cmp_to_key(resolve)) # type: ignore

idx1 = packets.index([[2]]) + 1
idx2 = packets.index([[6]]) + 1
print('part 2',idx1*idx2)