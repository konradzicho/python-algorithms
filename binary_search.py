def binary_search(lista, target_value):
  left_pointer = 0
  right_pointer = len(lista)-1
  middle_element_index = 0
  while(target_value!=lista[middle_element_index]):
    middle_element_index = int((left_pointer+right_pointer)/2)
    if(lista[middle_element_index] < target_value):
      left_pointer = middle_element_index+1
    elif(lista[middle_element_index] > target_value):
      right_pointer = middle_element_index-1
    else:
      pass
  return middle_element_index

print(4 == binary_search([0, 2, 4, 6, 8, 10, 12, 14], 8))

print(7 == binary_search([1, 2, 4, 6, 10, 16, 22, 25, 27, 28, 29, 33, 35, 40, 50], 25))
print(4 == binary_search([1, 2, 4, 6, 10, 16, 22, 25, 27, 28, 29, 33, 35, 40, 50], 10))
print(11 == binary_search([1, 2, 4, 6, 10, 16, 22, 25, 27, 28, 29, 33, 35, 40, 50], 33))
print(13 == binary_search([1, 2, 4, 6, 10, 16, 22, 25, 27, 28, 29, 33, 35, 40, 50], 40))

print(0 == binary_search([1,3,4,6,7,8,10,13,14,18,19,21,24,37,40,45,71], 1))
print(5 == binary_search([1,3,4,6,7,8,10,13,14,18,19,21,24,37,40,45,71], 8))
print(8 == binary_search([1,3,4,6,7,8,10,13,14,18,19,21,24,37,40,45,71], 14))
print(14 == binary_search([1,3,4,6,7,8,10,13,14,18,19,21,24,37,40,45,71], 40))
print(16 == binary_search([1,3,4,6,7,8,10,13,14,18,19,21,24,37,40,45,71], 71))
