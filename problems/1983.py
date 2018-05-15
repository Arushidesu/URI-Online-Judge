n = int(input())
ide = nota = 0
for i in range(n):
    a, b = map(float, input().split())
    if i == 0: ide, nota = a, b
    elif b > nota: ide, nota = a, b
if nota >= 8: print(int(ide))
else: print("Minimum note not reached")
