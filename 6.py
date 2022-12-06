f = open("inputs/6.txt")
data = f.read()

i = None

for idx,letter in enumerate(data[3:]):
  if len(set(data[idx:idx+4])) == 4:
    i =  idx+4
    break

print(f"part 1: {i}")

for idx,letter in enumerate(data[13:]):
  if len(set(data[idx:idx+14])) == 14:
    i =  idx+14
    break

print(f"part 2: {i}")
