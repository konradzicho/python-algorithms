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

###################################################

def merge_sort(list1):
  new_list = []
  for i in range (len(list1)):
    new_list.append([list1[i]])
  while len(new_list) > 1 :
    new_list.append(merge(new_list.pop(0),new_list.pop(0)))

  if new_list:
    return new_list[0]
  else:
    return []
 
####################################################
print([0, 1, 2, 4, 5, 6, 7, 8] == merge_sort([2,5,8,0,1,4,6,7]))
print([] == merge_sort([]))
print([1] == merge_sort([1]))
print([0, 2, 4, 6, 8, 10] == merge_sort([10, 8, 6, 4, 2, 0]))
