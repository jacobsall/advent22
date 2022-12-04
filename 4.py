def lineToPairs(line):
  return [pair.split('-') for pair in line.split(',')]

def pairToRanges(pair):
  return [set(range(int(rangeStr[0]),int(rangeStr[1])+1)) for rangeStr in pair]

f = open("inputs/4.txt")
data = f.read()

lines = data.split('\n')
pairs = [lineToPairs(line) for line in lines]
ranges = [pairToRanges(pair) for pair in pairs]

print(ranges)

subsets = [1 if r[0].issubset(r[1]) or r[1].issubset(r[0]) else 0 for r in ranges]

print(f"part 1: {sum(subsets)}")

intersections = [1 if r[0].intersection(r[1]) else 0 for r in ranges]

print(f"part 2: {sum(intersections)}")