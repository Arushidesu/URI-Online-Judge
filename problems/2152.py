n = int(input())
for i in range(n):
    h, m, o = input().split()
    if len(h) == 1:
        h = "0" + h
    if len(m) == 1:
        m = "0" + m
    if o == '1':
        print("{}:{} - A porta abriu!" .format(h, m))
    else:
        print("{}:{} - A porta fechou!" .format(h, m))
