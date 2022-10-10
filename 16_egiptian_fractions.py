import math 

def egyptian_frack(numerador, denominador):
  #creating our list of denominators for our egyptian fractions 
  egypt_lst = []
  
  while numerador != 0:
    
    x = math.ceil(denominador/numerador )
    egypt_lst.append(x)
    print(egypt_lst)
    
    numerador = x * numerador - denominador
    denominador *= x
    print(denominador)
    
    
  str = ""
  
  for one in egypt_lst:
    str += "1/{0} + ".format(one)
    
  final_str = str[:-3]
  
  return final_str


print(egyptian_frack(7,12))  