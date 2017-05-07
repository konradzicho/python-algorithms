def swap(lista, index1, index2):
  buffer = lista[index1]
  lista[index1] = lista[index2]
  lista[index2] = buffer
  return lista
  
print(swap([2, 7], 0, 1))

print([7, 2] == swap([2, 7], 0, 1))
print([7, 2] == swap([2, 7], 1, 0))
print([5, 11, 7] == swap([5, 7, 11], 1, 2))
