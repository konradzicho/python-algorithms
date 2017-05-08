def swap(lista, index1, index2):
  buffer = lista[index1]
  lista[index1] = lista[index2]
  lista[index2] = buffer
  return lista

def maxElement(lista):
  maxElementIndex = 0
  maxElementValue = lista[0]
  for index in range(len(lista)-1):
    if (maxElementValue<lista[index+1]):
      maxElementIndex = index+1
      maxElementValue = lista[index+1]
  return maxElementIndex

def selection_sort(lista):
  for index in range(len(lista)):
    nowa_lista = lista[0:len(lista)-index]
    max_element_index = maxElement(nowa_lista)
    swap(lista, max_element_index, len(lista)-1-index )
  return lista
    
print([0, 1, 5, 7, 9] == selection_sort([7, 5, 1, 9, 0]))
print([0, 1, 7, 8, 10, 10] == selection_sort([10, 10, 7, 8, 1, 0]))
