import networkx as nx
import matplotlib.pyplot as plt
from copy import deepcopy

def explore(G,u,unvisited,time=0,flow=0,pressure=0,path=[],max_time=30,paths=[]):
  if not unvisited:
    pressure += (max_time-time) * flow
    paths.append((path,pressure))
    return pressure
  for v in unvisited:
    new_time = G.get_edge_data(u,v)['weight'] + 1
    if new_time == 1 or time + new_time > max_time:
      new_pressure= (max_time - time) * flow
      paths.append((path,pressure+new_pressure))
      continue
    new_pressure = flow * new_time
    explore(G, v, unvisited=unvisited-{v}, time=time+new_time, flow=flow + G.nodes[v]['f'],
    pressure=pressure+new_pressure, path=path+[v] ,max_time=max_time, paths=paths)

f = open("inputs/16.txt")
data = f.read().split('\n')
sublines = [[subline for subline in line.split(';')] for line in data]

graph = nx.DiGraph()

for subline in sublines:
  split = subline[0].split(' ')
  valve = split[1]
  flow = int(split[-1].split('=')[1])
  graph.add_node(valve,f=flow)

  split = subline[1].split(',')
  for s in split:
    v = s[-2:len(s)]
    graph.add_edge(valve,v,weight=1)

newedges = []
for u in graph.nodes:
  for v in graph.nodes:
    if u != v:
      w = nx.dijkstra_path_length(graph,u,v)
      if w != 0:
        newedges.append((u,v,w))

graph = nx.create_empty_copy(graph)

for u,v,w in newedges:
  graph.add_edge(u,v,weight=w)

nodes = deepcopy(graph.nodes)
for node in nodes:
  if graph.nodes[node]['f'] <= 0 and node != 'AA':
    graph.remove_node(node)

time = 30
start = 'AA'

paths = []
explore(graph,start,set(graph.neighbors(start)),max_time=time,paths=paths)
print("part 1: ",(sorted(paths,key=lambda x:-x[1]))[0])


if False:
  pos=nx.spring_layout(graph)
  nx.draw(graph,pos,with_labels=True)
  labels = nx.get_edge_attributes(graph,'weight')
  nx.draw_networkx_edge_labels(graph,pos,edge_labels=labels)
  plt.show()