def swap(lista, index1, index2):
  buffer = lista[index1]
  lista[index1] = lista[index2]
  lista[index2] = buffer
  return lista

def bubblesort(lista):
  operationsCounter = 1
  while (operationsCounter):
    operationsCounter=0
    for index in range(len(lista)-1):
      if (lista[index]>lista[index+1]):
        swap (lista, index, index+1)
        operationsCounter += 1
  return lista
    
print([2, 5, 7, 9] == bubblesort([9, 5, 2, 7]))
print([2, 5, 7, 9] == bubblesort([5, 7, 9, 2]))
print([2, 5, 7, 9] == bubblesort([7, 9, 2, 5]))
print([2, 5, 7, 9] == bubblesort([9, 7, 5, 2]))
