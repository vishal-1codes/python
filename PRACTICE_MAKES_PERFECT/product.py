#Here we * or multiply all list value and return one value
def product(list):
      total=1;
      for num in list:
          total*=num
          return total
print(product([1,2,3]))