from collections import deque
import numpy as np
import operator

def func(x,op):
  a = x if op[0] == 'old' else int(op[0])
  b = x if op[2] == 'old' else int(op[2])
  if op[1] == '+':
    return operator.add(a,b)
  else:
    return np.multiply(a,b)

def throw_to(x,div):
  if np.mod(x, div[0]) == 0:
    return str(div[1])
  return str(div[2])

f = open("inputs/11.txt")
data = f.read().split('\n\n')
monkeys = {}
PART1 = False
ROUNDS = 20 if PART1 else 10000

for block in data:
  lines = block.split('\n')
  
  _id = lines[0].split(' ')[1][0]
  items = deque([int(number) for number in lines[1].split(': ')[1].split(', ')])
  op = lines[2].split('new = ')[1].split(' ')
  div = [int(line.split(' ')[-1]) for line in lines[3:6]]

  monkeys[_id] = {
    'items': items,
    'op': op,
    'div': div,
    'inspects': 0
  }

mod_factor = np.prod([monkey['div'][0] for monkey in monkeys.values()])

for i in range(1,ROUNDS+1):
  for monkey in monkeys.values():
    if not monkey['items']:
      continue
    
    for j in range(0,len(monkey['items'])):
      old = monkey['items'].popleft()
      new = func(old,monkey['op']) // 3 if PART1 else func(old,monkey['op']) % mod_factor
      to = throw_to(new,monkey['div'])
      monkeys[to]['items'].append(new)
      monkey['inspects'] += 1

  if i in [1,20,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]:
    print()
    print('== After round ',i,' ==')
    [print('Monkey ',_id,' : ',value['inspects']) for _id,value in monkeys.items()]

inspects = list(reversed(sorted([value['inspects'] for value in monkeys.values()])))
print('part 1: ',inspects[0]*inspects[1])