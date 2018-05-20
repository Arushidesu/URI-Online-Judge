a, b, c = map(int, input().split())
x, y, z = map(int, input().split())
soma = 0
if x > a:
  soma += abs(x - a)
if y > b:
  soma += abs(y - b)
if z > c:
  soma += abs(z - c)
print(0 if a > x and b > y and c > z else soma)
