inventory = {
  'gold' : 500,
  'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
  'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}



# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

# We create new key and value in dic
inventory['pocket'] = ['seashell','strange berry','lint']
#We remove key value here
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
#We add 50 to gold key value
inventory['gold']=inventory['gold'] + 50