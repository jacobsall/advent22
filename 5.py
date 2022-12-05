from collections import deque


f = open("inputs/5.txt")
data = f.read()
split = data.split('\n\n')

crateLines = split[0].split('\n')[::-1]
stackIdxs = [crateLines[0].index(index) for index in crateLines[0].split()]
moves = [[int(i) for i in line.split(' ') if i.isnumeric()] for line in split[1].split('\n')]

def resetStacks():
  stacks =  [deque() for _ in stackIdxs]
  for line in crateLines[1:]:
    for idx, str_idx in enumerate(stackIdxs):
      if line[str_idx].isalpha():
        stacks[idx].append(line[str_idx])
  return stacks
    
stacks = resetStacks()
for move in moves:
  for i in range(0,move[0]):
    top = stacks[move[1]-1].pop()
    stacks[move[2]-1].append(top)
      
output = "".join([stack[-1] for stack in stacks])

print(f"part 1: {output}")


stacks = resetStacks()
for move in moves:
  tops = deque()
  for i in range(0,move[0]):
    tops.appendleft(stacks[move[1]-1].pop())
  stacks[move[2]-1].extend(tops)
      
output = "".join([stack[-1] for stack in stacks])

print(f"part 2: {output}")


