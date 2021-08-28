#a function can call another function
#In 2nd function we add output of 1st function
def one_good_turn(n):
  return n + 1
    
def deserves_another(n):
  return one_good_turn(n) + 2