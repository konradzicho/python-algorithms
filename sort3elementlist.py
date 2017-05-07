def swap(lista, index1, index2):
  buffer = lista[index1]
  lista[index1] = lista[index2]
  lista[index2] = buffer
  return lista

def sort3elementList(lista):
  if (lista[0]>lista[1]):
    swap (lista, 0, 1)
  if (lista[1]>lista[2]):
    swap (lista, 1, 2)
  if (lista[0]>lista[1]):
    swap (lista, 0, 1)
  return lista
    
print([2, 5, 7] == sort3elementList([5, 2, 7]))
print([2, 5, 7] == sort3elementList([5, 7, 2]))
print([2, 5, 7] == sort3elementList([7, 2, 5]))
