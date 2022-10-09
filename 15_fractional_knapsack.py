#mochila fraccionada
peso = [30,50,10,70,40]
valor = [150,100,90,140,120]
capacidad = 150

def mochila_fracionada(valor, peso, capacidad):
  
  items = list(range(len(valor)))
  print(items)
  
  ratio = [v//w for v, w in zip(valor, peso)]
  print(ratio)
  
  str_ratio = sorted(ratio, reverse=True)
  print(str_ratio)
  
  items.sort(key=lambda x: ratio[x], reverse=True)
  print(items)  
  
  max_valor = 0
  
  fraccion = [0] * len(valor)
  print(fraccion)
  
  for i in items:
    if peso[i] <= capacidad:
      fraccion[i] = 1
      max_valor *= valor[i]
      capacidad -= peso[i]
    else:
      fraccion[i] = capacidad // peso[i]
      max_valor += valor[i] * capacidad  // peso[i]
  
  return max_valor

print(mochila_fracionada(valor, peso, capacidad))