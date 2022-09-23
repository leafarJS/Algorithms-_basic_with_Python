# Recursividad | la funcion se llama a si misma 

#factorial  n!
#ejemplo n! = 5
#n! = (n*0)*(n*1)*(n*2)*(n*3)*(n*4) = 120

def factorial(n):
  factorial = 1
  for i in range(2, n + 1):
    factorial *= i
  return factorial 

print(factorial(5))

def recursividad_factorial(n):
  if n == 1:
    return n
  else:
    temporal = recursividad_factorial(n-1)
    salida = temporal * n
  return salida 


print(recursividad_factorial(5))

#Permutaciones 
#permutación es cuando se toma un conjuto de elementos y se encuentran todas las combinaciones posibles 
#permutaciones de ABC 
print(recursividad_factorial(3))

def permutaciones(str, packet = ""):
  if len(str) == 0:
    print(packet)
  else:
    for i in range(len(str)):
      
      letra = str[i]
      frente = str[0:i]
      atras = str[i+1:]
      juntos = frente + atras
      #print(juntos)
      permutaciones(juntos, letra + packet)


print(permutaciones("ABC"))

print("Algoritmo mas eficiente que el anterior")

def permutations(str):
  for p in range(factorial(len(str))):
    print("".join(str))
    i = len(str) - 1
    while i > 0 and str[i - 1] > str[i]:
      i -= 1
    str[i:] = reversed(str[i:])
    if i > 0:
      q = i 
      while str[i - 1] > str[q]:
        q += 1
      temp = str[i - 1]
      str[i - 1] = str[q]
      str[q] = temp
      


cadena = "ABC"
cadena = list(cadena)

permutaciones(cadena)  



