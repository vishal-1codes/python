#Dictionary is just a collection of keys and values.
my_dict={
  "Name":"vishal",
  "Age":21,
  "Color":"brown"
}

print(my_dict.keys())
print(my_dict.values())

for number in range(5):
  print(number,)

for letter in "Eric":
  print(letter,) 

for key in my_dict:
  print(key, my_dict[key])

#Here we print all key value in simple format
#Note that the trailing comma ensures that we keep printing on the same line.

#.items() method doesn’t return key/value pairs in any specific order.
#It return list items