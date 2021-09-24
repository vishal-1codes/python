#Note that using the & operator can only result in a number that is less than or equal to the smaller of the two values.
#0 & 0 = 0
#0 & 1 = 0
#1 & 0 = 0
#1 & 1 = 1

print(bin(0b1110 & 0b101))