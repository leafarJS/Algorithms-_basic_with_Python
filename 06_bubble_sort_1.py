def swap(x, i, j):
  temp = x[i] 
  x[i] = x[j]
  x[j] = temp


def bubble_sort(x):
  iteraciones = 0
  
  for i in x:
    for j in range(len(x) - 1):
      iteraciones += 1
      if x[j] > x[j + 1]:
        swap(x, j, j + 1)
  return x, iteraciones
  
  
arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(bubble_sort(arr))