#In this code we have to return factorial number that can be if 3 then we have to return 3*2*1=6
#In this code we first defined toatl=1;
#Then we add condition while
#Then agin we minus -1 from return value

def factorial(x):
    total = 1
    while x>0:
        total *= x
        x-=1
    return total
  
print(factorial(5))