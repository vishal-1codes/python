#Here we simply replace A and a with X
# , most imp in after print statement 
phrase = "A bird in the hand..."

# Add your for loop
for char in phrase:
  if char == "A" or char == 'a':
    print('X'),
  else:
    print(char),

#Don't delete this print statement!
print