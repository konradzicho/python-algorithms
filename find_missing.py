def find_missing(list1):
  for i in range(max(list1)+1):
    if not (i in list1):
      return i

print(1 == find_missing([0, 2, 3, 4]))
print(0 == find_missing([1, 2, 3]))
print(5 == find_missing([0, 1, 2, 3, 4, 6]))
print("**************************"+"\n")


#ALTERNATIVELY, WITHOUT IN FUNCTION
def find_missing2(list1):
  for i in range(len(list1)+1):
    found = False
    for j in range(len(list1)):
      if (i==list1[j]):
        found = True
        break
    if (found == False):
      return i

print(3 == find_missing2([0, 1, 2, 4]))
print(0 == find_missing2([1, 2, 3]))
print(5 == find_missing2([0, 1, 2, 3, 4, 6]))
print("**************************"+"\n")

#ALTERNATIIVE, IMPROVING COMPUTATIONAL COMPLEXITY
def find_missing3(list1):
  list1.sort()
  for i in range(len(list1)):
    if (i != list1[i]):
      return i
      
print(3 == find_missing3([0, 1, 2, 4]))
print(0 == find_missing3([1, 2, 3]))
print(5 == find_missing3([0, 1, 2, 3, 4, 6]))
print("**************************"+"\n")

#ALTERNATIVE, IMPROVING COMPUTATIONAL COMPLEXITY EVEN MORE
def find_missing4(list1):
  expected_sum = 0
  for i in range(len(list1)+1):
    expected_sum += i
  return (expected_sum - sum(list1))
  
print(3 == find_missing4([0, 1, 2, 4]))
print(0 == find_missing4([1, 2, 3]))
print(5 == find_missing4([0, 1, 2, 3, 4, 6]))
print(4 == find_missing4([6, 2, 5, 0, 1, 3]))
print("**************************"+"\n")
  
