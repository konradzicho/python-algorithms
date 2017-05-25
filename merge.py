def merge(list1, list2):

  list_joined = []
  while (list1 and list2):
    if list1[0]<list2[0]:
      list_joined.append(list1.pop(0))
    else:
      list_joined.append(list2.pop(0))
  if (not list1):
    list_joined.extend(list2)
  elif (not list2):
    list_joined.extend(list1)
  return list_joined

print([1, 2, 3, 4, 5, 6, 7, 9] == merge([1, 3, 5, 7],[2, 4, 6, 9]))
print([1, 2, 3, 4, 5, 6, 7, 8] == merge([1, 2, 3, 4],[5, 6, 7, 8]))
print([1, 1, 1, 1, 2, 2, 2, 2] == merge([1, 1, 1, 1],[2, 2, 2, 2]))
print([1, 1, 2, 3, 4, 20, 50, 100] == merge([1, 20, 50, 100],[1, 2, 3, 4]))
print([1, 2, 3, 4, 5] == merge([1, 2, 3, 4, 5],[]))
print([] == merge([],[]))
