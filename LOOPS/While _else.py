#Here we crete game , whenever you press run code generate 4 value if code get 3 value in between 4 then you win another wise false execute.
#An we not use ; in break
import random

print("Lucky Numbers! 3 numbers will be generated.")
print("If one of them is a '5', you lose!")

count = 0
while count < 3:
  num = random.randint(1, 6)
  print(num)
  if num == 5:
    print("Sorry, you lose!")
    break
  count += 1
else:
  print("You win!")