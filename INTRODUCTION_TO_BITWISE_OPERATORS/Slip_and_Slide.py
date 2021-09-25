#Finally, you can also use the left shift (<<) and right shift (>>) operators to slide masks into place.
def flip_bit(number, n):
    
    bit_to_flip = 0b1 << (n -1)
    result = number ^ bit_to_flip
    return bin(result)