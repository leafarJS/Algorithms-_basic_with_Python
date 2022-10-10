"""
TODO: 
1. city 1 starting and ending point
2. (n-1)! generating all permutations factorial posible of city
3.  calculate cost of every permutations 
4. return min cost 
"""
from itertools import permutations
#point in plot 
vertice = 4

def travel_salesman_problem(graph, s):
  #store all vertices 
  vertex = []
  for i in range(vertice):
    if i != s:
      vertex.append(i)
      print(vertex)
      
  min_path = []
  next_permutation = permutations(vertex)
  
  for i in next_permutation:
    current_path_weight = 0
    
    k = s
    
    for j in i:
      current_path_weight += graph[k][j]
      print(j,i, current_path_weight, graph[k][j])
      k = j
    
    current_path_weight += graph[k][s]
    min_path.append(current_path_weight)
    x = sorted(min_path)
  
  return x[0]


if __name__ == "__main__":
  # matrix representation of graph
  graph =[[0,10,15,20],
          [10,0,35,25],
          [15,35,0,30],
          [20,25,30,0]]
  s = 0
# imagen 1:59:12min
  
print(travel_salesman_problem(graph, s))