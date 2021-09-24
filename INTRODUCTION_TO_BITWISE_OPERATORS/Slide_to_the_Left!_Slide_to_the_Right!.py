shift_right = 0b1100
shift_left = 0b1

# Your code here!
#In >> 2 = 2 zeros cut
#in << 2 = 2 zeros add
shift_right = shift_right >> 2
shift_left = shift_left << 2

print(bin(shift_right))
print(bin(shift_left))