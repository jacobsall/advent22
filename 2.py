move_points = {
  'X' : 1,
  'Y' : 2,
  'Z' : 3
}

round_points = {
  'AX' : 3, 
  'AY' : 6,
  'AZ' : 0,
  'BX' : 0, 
  'BY' : 3,
  'BZ' : 6,
  'CX' : 6, 
  'CY' : 0,
  'CZ' : 3,
}

winning_move = {
  'AX' : 'Z', 
  'AY' : 'X',
  'AZ' : 'Y',
  'BX' : 'X', 
  'BY' : 'Y',
  'BZ' : 'Z',
  'CX' : 'Y', 
  'CY' : 'Z',
  'CZ' : 'X',
}

res_points = {
  'X' : 0,
  'Y' : 3,
  'Z' : 6
}



f = open("inputs/2.txt")
data = f.read()

moves = [row.split(' ') for row in data.split('\n')]

points = [move_points[you] + round_points[opp+you] for opp,you in moves]
print(f"part 1: {sum(points)}")

points = [move_points[winning_move[opp+res]] + res_points[res] for opp,res in moves]
print(f"part 2: {sum(points)}")