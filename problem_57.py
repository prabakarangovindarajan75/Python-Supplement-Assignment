# Problem 57: Find LCM of two numbers
# Find and fix the error

def lcm(a, b):
    return abs(a * b) // gcd(a, b)
