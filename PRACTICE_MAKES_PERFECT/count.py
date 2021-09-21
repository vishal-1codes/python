#Here we count how many time 2nd number apperes in 1st list
def count(sequence, item):
    count = 0
    for i in sequence:
        if i == item:
            count += 1
    return count
  
print(count([1, 2, 1, 1], 1))