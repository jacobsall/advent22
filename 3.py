def letterToPriority(letter):
  if letter.isupper():
    return 27 - ord('A') + ord(letter)
  return 1 - ord('a') + ord(letter)


f = open("inputs/3.txt")
data = f.read()
lines = data.split('\n')

total = 0

for backpack in lines:
  size = len(backpack)
  comp1 = backpack[0:int(len(backpack)/2)]
  comp2 = backpack[int(len(backpack)/2):len(backpack)]

  letter = set(comp1).intersection(comp2).pop()
  total += letterToPriority(letter)

print(f"part 1: {total}")


total = 0
index = 0
while index < len(lines):
  b1,b2,b3 = lines[index:index+3]
  label = set(b1).intersection(b2).intersection(b3).pop()
  total += letterToPriority(label)
  index += 3

print(f"part 2: {total}")