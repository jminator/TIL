# itertools.product() gives us cartesian products

from itertools import product

a = map(int, input().split())
b = map(int, input().split())
print(" ".join(map(str, product(a, b)))) # to separate by space. 
# or this:
print(*product(a, b)) # '*' is an unpack operator

