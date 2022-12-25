import numpy as np
f = open("inputs/25.txt")
data = f.read().splitlines()

translate = {
  '=': -2,
  '-': -1,
  '0': 0,
  '1': 1,
  '2': 2
}

def convert(line):
  return sum([pow(5,idx)*translate[char] for idx,char in enumerate(line[::-1])])

def invert(num):
  rems = ""
  lst = ['0','1','2','=','-','0']
  carry = 0
  while num != 0 or carry:
    rem = num % 5 + carry
    rems = lst[rem] + rems
    num //= 5
    carry = 1 if rem in [3,4,5] else 0
  return rems

ans = sum([convert(line) for line in data])
print('base 10: ', ans)

inverted = invert(ans)
print('snafu: ', inverted)

