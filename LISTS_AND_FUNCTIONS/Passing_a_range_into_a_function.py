#The range function has three different versions:
# range(stop)
# range(start, stop)
# range(start, stop, step)

def my_function(x):
  for i in range(0, len(x)):
    x[i] = x[i]
    return x

print(my_function(range(0,3))) # Add your range between the parentheses!