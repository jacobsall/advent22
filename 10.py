import numpy as np

f = open("inputs/10.txt")
data = f.read().split('\n')
instructions = [line.split(' ') for line in data]

# print(len(instructions))

x = 1
total = 0

cycles = []
CRT = []

def checkCycle():
  if len(cycles) > 0 and len(cycles) in [20 + 40*x for x in range(0,6)]:
    return len(cycles) * cycles[-2]
  return 0

def doCRT():
  if len(CRT) % 40 in [x-1,x,x+1]:
    CRT.append('#')
  else:
    CRT.append('.')

for instr in instructions:
  if instr[0] == 'addx':
    doCRT()
    cycles.append(x)
    total += checkCycle()

    doCRT()
    x += int(instr[1])
    cycles.append(x)
    total += checkCycle()
  else:
    doCRT()
    cycles.append(x)
    total += checkCycle()
  

print("part 1: ",total)


[CRT.insert(i,'\n') for i in [40,81,122,163,204]]
print(''.join(CRT))
