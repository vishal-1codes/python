#Here we first check whether value is int or float if value have inbetween then return abs value that can be abslolute value in positive
#if not then return Nope

def distance_from_zero(a):
  if type(a)==int or type(a)==float:
    return abs(a)
  else:
    return "Nope"

distance_from_zero(2)