#In this code we find out index of any element 
#using  .index("name")
#also we insert element using index and value
#eg - animals.insert(2,"cobra")
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")# Use index() to find "duck"

# Your code here!
animals.insert(duck_index,"cobra")

print(animals) # Observe what prints after the insert operation