#SoftwareAG question 
#Here we find how many times fizz word present in list x .

def fizz_count(x):
  count = 0
  for item in x:
    if item == "fizz":
      count = count + 1
  return count