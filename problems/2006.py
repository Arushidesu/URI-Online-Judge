t = int(input())
a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])
print(a.count(t))
