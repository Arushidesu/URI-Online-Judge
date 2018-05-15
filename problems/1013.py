a, b, c = input().split(" ")
mab = (int(a) + int(b) + abs(int(a) - int(b))) / 2
r = (int(mab) + int(c) + abs(int(mab) - int(c))) / 2
print("%d eh o maior" %r)
