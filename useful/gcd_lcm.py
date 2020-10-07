from math import gcd

# (최소공배수 * 최대공약수 = a * b)

# gcd (greatest common divisor)

print(gcd(16, 4))

# lcm (largest common multiple)

def lcm(a, b):
    return abs(a*b) // gcd(a, b)