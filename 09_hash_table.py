# una tabla hash usa una función hash para calcular un indice tambien llamado codigo hash en matrices de cubos o ranuras desde las cuales se  puede encontrar el valor deseado.
# durante la busqueda la clave se codifica y el hash resultante indica donde se almacenara el valor correspondiente en  muchas situaciones. las tablas hash resultan ser, en promedio, mas eficientes que los arboles de busqueda o cualquier otra estructura de busqueda de tablas. por esta razon se usan amplimamente en muchos tipos de software de computadora, particularmente para arreglos asociativos, indices de bases de datos, caches y conjuntos. 

#RESUMEN Con las tablas hash se puede almacenar, recuperar y eliminar datos de forma unica en función de su clave unica

# insert (key, value)
# get (key)
# delete (key)
# separete chaining 
# local addressing 
class Hash_table:
  def __init__(self):
    self.table = [None] * 127
    
  #función hash
  def hash_functions(self, value):
    key = 0
    for i in range(0, len(value)):
      key += ord(value[i])
    return key % 127
  
  # Función hash
  def Hash_func(self, value):
        key = 0
        for i in range(0,len(value)):
            key += ord(value[i])
        return key % 127

  def Insert(self, value): # Metodo para ingresar elementos
        hash = self.Hash_func(value)
        if self.table[hash] is None:
            self.table[hash] = value
   
  def Search(self,value): # Metodo para buscar elementos
        hash = self.Hash_func(value)
        if self.table[hash] is None:
            return None
        else:
            return hex(id(self.table[hash]))
          
  def Remove(self, value):
    hash = self.Hash_func(value)
    if self.table[hash] is None:
      print(f"No hay elementos con ese valor {value}")
    else:
      print(f"Elemento con valor {value} eliminado")
      self.table[hash] is None
  
  
result = Hash_table()
