import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

f = open("inputs/12.txt")
data = f.read().split('\n')

grid = np.array([np.array([1000 if char == 'E' else (0 if char == 'S' else ord(char)) for char in line]) for line in data])

s = np.where(grid == 0)
S = f"{s[0][0]},{s[1][0]}"
grid[s[0][0]][s[1][0]] = ord('a')

e = np.where(grid == 1000)
E = f"{e[0][0]},{e[1][0]}"
grid[e[0][0]][e[1][0]] = ord('z')

print(grid)
# print(s,e)

graph = nx.DiGraph()

for i,row in enumerate(grid):
  for j,col in enumerate(row):
    edges = []
    if i > 0 and grid[i-1][j] <= col+1:#in [col-1,col,col+1]:
      edges.append((f'{i},{j}',f'{i-1},{j}'))
    if i < len(grid)-1 and grid[i+1][j] <= col+1:#in [col-1,col,col+1]:
      edges.append((f'{i},{j}',f'{i+1},{j}'))
    if j > 0 and grid[i][j-1] <= col+1:#in [col-1,col,col+1]:
      edges.append((f'{i},{j}',f'{i},{j-1}'))
    if j < len(row)-1 and grid[i][j+1] <= col+1:#in [col-1,col,col+1]:
      edges.append((f'{i},{j}',f'{i},{j+1}'))
    graph.add_edges_from(edges)


path = nx.dijkstra_path(graph,S,E)
print('part 1: ', len(path)-1)

lowest = np.where(grid == ord('a'))
paths = []
for x,y in zip(lowest[0],lowest[1]):
  start = f"{x},{y}"
  try:
    paths.append(nx.dijkstra_path_length(graph,start,E))
  except nx.NetworkXNoPath:
    continue
print('part 2: ', sorted(paths)[0])
# print(path)
# nx.draw_spectral(graph,with_labels=True)
# plt.show()