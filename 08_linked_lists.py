# una lista enlazada o anidada es una colección lineal de elementos de datos cuyo orden no esta dado por su ubicación fisica en la memoria, sino que cada elemento apunta al siguiente.
# Es una estructura de datos que consiste en una colección de nodos que juntos representan una secuencia en su forma mas basica , cada nodo contiene datos y una referencia, en otras palabras, un enlace al siguiente nodo en la secunencia. Esta estructura permite la inserción o eliminación eficiente de elementos de cualquier posición en la secuencia durante la iteración. variantes mas complejas y enlaces adicionales que permiten una inserción o eliminacion mas eficiente de nodos en posiciónes arbitrarias; un inconveniente de las listas enlazadas es que el tiempo de acceso es lineal y dificil de canalizar. Algunos dicen que las listas enlazadas se encuentran entre las mas simples y comunes estructuras de datos

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class LinkedList:
  def traversal(self):
    first = self.head
    while first:
      print(first.data)
      first = first.next
  
  
  def insert_new_header(self, new_data):
    new_node = Node(new_data)
    new_node.next = self.head 
    self.head = new_node
  
  
  def search(self, x):
    temp = self.head
    while temp is not None:
      if temp.data == x:
        return True
      temp = temp.next
    else:
      return False
  
  
  def delete_node(self, data):      
    temp = self.head
    while temp is not None:
      if temp.data == data:
        break
      prev = temp
      temp = temp.next 
    prev.next = temp.next
  
  def delete_tail(self):
    temp = self.head
    while temp.next.next is not None:
      temp = temp.next 
    temp.next = None 
      
    
family = LinkedList()
family.head = Node("Bob")
wife = Node("Amy")
first_kid = Node("Max")
second_kid = Node("Jenny")

family.head.next = wife
wife.next = first_kid
first_kid.next = second_kid

#family.traversal()
family.insert_new_header("Jorge")
#print(family.search("Bob"))
family.delete_node("Bob")
family.delete_tail()
family.traversal()