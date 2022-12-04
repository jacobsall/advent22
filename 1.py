import sys
import numpy as np

f = open("inputs/1.txt")
data = f.read()

grouped = [np.sum([int(num) for num in group.split('\n')]) for group in data.split('\n\n')]

sortedList = list(reversed(sorted(grouped)))

part1 = sortedList[0]
print(f"part 1: {part1}")

part2 = np.sum(sortedList[0:3])
print(f"part 2: {part2}")



