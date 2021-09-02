#enumerate works by supplying a corresponding index to each element in the list that you pass it.
#using +1 we add index from 1 rather then 0
choices = ['pizza', 'pasta', 'salad', 'nachos']

print('Your choices are:')
for index, item in enumerate(choices):
  print(index+1, item)