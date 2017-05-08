
def maxElement(lista):
  maxElementIndex = 0
  maxElementValue = lista[0]
  for index in range(len(lista)-1):
    if (maxElementValue<lista[index+1]):
      maxElementIndex = index+1
      maxElementValue = lista[index+1]
  return maxElementIndex
    
print(0 == maxElement([9, 5, 2, 7]))
print(2 == maxElement([5, 7, 9, 2]))
print(1 == maxElement([7, 9, 2, 5]))
print(0 == maxElement([9, 7, 5, 2]))
print(3 == maxElement([9, 7, 5, 10]))
print(0 == maxElement([9, 7, 9]))
