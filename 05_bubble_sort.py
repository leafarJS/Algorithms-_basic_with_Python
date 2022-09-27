def bubble_sort(x):
  iteraciones = 0
  for i in range(len(x)):
    for j in range(len(x) - i - 1):
      iteraciones += 1
      if x[j] > x[j+1]:
        x[j], x[j+1] = x[j+1], x[j]
  return x, iteraciones


arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(bubble_sort(arr))