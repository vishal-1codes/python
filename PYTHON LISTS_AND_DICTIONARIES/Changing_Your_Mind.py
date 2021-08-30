#for delete dict keys NOTE - key name use 
#eg del dict_name[key_name] 
#For assign new value  NOTE - new value in "" ''
#eg dict_name[key] = new_value

# key - animal_name : value - location 
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}
# A dictionary (or list) declaration may break across multiple lines

# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']

del zoo_animals["Bengal Tiger"]

del zoo_animals["Sloth"]

zoo_animals['Rockhopper Penguin']="Tiger"


print(zoo_animals)