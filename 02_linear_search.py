#busqueda lineal, recorrer el arreglo hasta encontrar el objetivo

def linear_search(arr, target):
    for i in range(len(arr)):
      if arr[i] == target:
        print(arr[i])
 
     
arreglo = [50,20,45,1,12,6,89,19,7,8,98,64,3213,654]
linear_search(arreglo, 20)
linear_search(arreglo, 120)
linear_search(arreglo, 1)