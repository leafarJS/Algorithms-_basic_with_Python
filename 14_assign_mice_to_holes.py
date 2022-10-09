def assignHols(mice, holes):
  
  #base - num of mice and holes should be the same
  if len(mice) != len(holes):
    return "Number of mice and holes not the same"
  
  
  #sort first
  mice.sort()
  holes.sort()
  
  #finding max difference between it nice and hole
  max_diff = 0
  
  for i in range(len(mice)):
    if max_diff < abs(mice[i] - holes[i]):
      max_diff = abs(mice[i] - holes[i])
      
    return max_diff
  
m = [4,-4,2]
h = [4,0,5]

min_time = assignHols(m, h)

print(f"the last mouse gets into the hole in time: {min_time}")
  