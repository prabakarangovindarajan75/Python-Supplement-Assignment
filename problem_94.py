# Problem 94: Count bits set to 1
# Find and fix the error

def count_set_bits(n):
    count = 0
    while n:
        n &= (n - 1)
        count += 1
    return count

