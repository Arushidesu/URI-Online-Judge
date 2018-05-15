from math import sqrt
n = int(input())
r = ((((1 + sqrt(5)) / 2) ** n) - (((1 - sqrt(5)) / 2) ** n)) / sqrt(5)
print("%.1f" %r)
