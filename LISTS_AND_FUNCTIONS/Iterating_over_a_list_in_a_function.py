#for item in list:
#print item
#Method 1 is useful to loop through the list, but it’s not possible to modify the list this way.

# for i in range(len(list)):
#       print list[i]
#Method 2 uses indexes to loop through the list, making it possible to also modify the list if needed.

#Here we count the number of list 
n = [3, 5, 7]

def total(numbers):
  result = 0
  for i in range(0,len(numbers)):
    result += numbers[i]
  return result