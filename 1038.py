x, y = input().split(" ")
x, y = int(x), int(y)
if 1 == x:
    r = y * 4.00
elif 2 == x:
    r = y * 4.50
elif 3 == x:
    r = y * 5.00
elif 4 == x:
    r = y * 2.00
elif 5 == x:
    r = y * 1.50
r = "%.2f" % r
print("Total: R$ %s" %r)
