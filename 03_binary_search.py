def binary_search(arr, start, end, target):
    while start <= end:
      middle  = int((start + end) / 2)
      if arr[middle] > target:
        start = int(middle + 1)
      elif arr[middle] < target:
        end = int(middle - 1)
      else:
        return middle

    return start
      
      
arreglo = [100,10,90,20,80,30,70,40,60,50]
objetivo = 10
resultado = binary_search(sorted(arreglo, reverse = False), 0, len(arreglo) -1 , objetivo )
if resultado != -1:
    print(f"El elemento esta presente en el arreglo: {resultado}")
else:
    print(f"El elemento no se encuentra presente en el array") 

    