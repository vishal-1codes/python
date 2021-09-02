#The difference is that the while loop will continue to execute as long as the condition is true.
#instead of executing if something is true, it executes while that thing is true.
#Here we print hello  0 and 9
count = 0

if count < 5:
  print("Hello, I am an if statement and count is", count)

while count < 10:
  print("Hello, I am a while and count is", count)
  count += 1