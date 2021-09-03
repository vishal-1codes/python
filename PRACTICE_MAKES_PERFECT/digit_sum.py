#In below example we first get input as a string then we apply for loop for each element in that can be join with + and also convert string element to int then return total.
def digit_sum(n):
  total = 0
  string_n = str(n)
  for char in string_n:
    total += int(char)
  return total

#Alternate Solution:

#def digit_sum(n):
#  total = 0
#  while n > 0:
#    total += n % 10
#    n = n // 10
#  return total
  
print(digit_sum(1234))