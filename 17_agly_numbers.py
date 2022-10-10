#recursive function for successive divisions

"""
TODO: Nota: para verificar en primer lugar que un numero es feo, dividimos el numero entre las mayores potencias divisibles de 2, 3, 5 , y si el numero se convierte en 1, entonces es un numero feo.

"""
def successive_div(x, y):
  while x % y == 0:
    x = x // y
  return x

print(successive_div(6,2))

def ugly_num_check(num):
  num = successive_div(num, 2)
  num = successive_div(num, 3)
  num = successive_div(num, 5)
  
  if num == 1:
    return True
  else:
    return False
  
  
print(ugly_num_check(6))



def nth_ugly(n):
  i = 1
  #ugly number count
  counter = 1
  
  #looping through all integers untill ugly count becomes n
  while n > counter:
    i += 1
    if ugly_num_check(i):
      counter +=1
  return i

number = 15
no = nth_ugly(number)
print(f"{number} ht ugly number is: {no}")


def ugly_number(n):
  dp_ugly = [0] * n
  dp_ugly[0] = 1
  
  u1 = u2 = u5 = 0
  
  mutiple_2 = 2
  mutiple_3 = 3
  mutiple_5 = 5
  
  for i in range(1, n):
    dp_ugly[i] = min(mutiple_2, mutiple_3, mutiple_5)
    
    if dp_ugly[i] == mutiple_2:
      u1 += 1
      multiple_2 = dp_ugly[u2] * 2
    
    if dp_ugly[i] == mutiple_3:
      u3 += 1
      multiple_3 = dp_ugly[u3] * 3
      
    if dp_ugly[i] == mutiple_5:
      u5 += 1
      multiple_5 = dp_ugly[u5] * 5
      
  return dp_ugly[n - 1]

print(f"{number} ht ugly number is: {ugly_number(number)}")