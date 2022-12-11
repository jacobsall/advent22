f = open("inputs/11.txt")
data = f.read().split('\n\n')

# print(data)
for block in data:
  lines = block.split('\n')
  
  _id = lines[0].split(' ')[1][0]
  items = [int(number) for number in lines[1].split(': ')[1].split(', ')]

  op = lines[2].split('new = ')[1].split(' ')
  
  def func(x):
    a = x if op[0] == 'old' else int(op[0])
    b = x if op[2] == 'old' else int(op[2])
    if op[1] == '+':
      return a + b
    else:
      return a * b

  print(func(1))