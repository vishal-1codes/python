print('Welcome to the Pig Latin Translator!')
#You can use .isalpha() to check that a string #doesn’t contain any non-letter characters
# Start coding here!
#isalpha is only check wheter any number in between string 
original = input("Enter a word:")
if len(original) > 0 and original.isalpha():
  print(original)
else:
  print("empty")