n = int(input())
a = input().split()
m2 = m3 = m4 = m5 = 0
for i in range(n):
    a[i] = int(a[i])
    if a[i] % 2 == 0:
        m2 += 1
    if a[i] % 3 == 0:
        m3 += 1
    if a[i] % 4 == 0:
        m4 += 1
    if a[i] % 5 == 0:
        m5 += 1
print(m2, "Multiplo(s) de 2")
print(m3, "Multiplo(s) de 3")
print(m4, "Multiplo(s) de 4")
print(m5, "Multiplo(s) de 5")
