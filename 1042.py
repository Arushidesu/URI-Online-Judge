x, y, z = map(int, input().split())
if x > y and y > z:
    print("%d\n%d\n%d\n" %(z, y, x))
elif x > z and z > y:
    print("%d\n%d\n%d\n" % (y, z, x))
elif y > x and x > z:
    print("%d\n%d\n%d\n" % (z, x, y))
elif y > z and z > x:
    print("%d\n%d\n%d\n" % (x, z, y))
elif z > x and x > y:
    print("%d\n%d\n%d\n" % (y, x, z))
elif z > y and y > x:
    print("%d\n%d\n%d\n" % (x, y, z))
print("%d\n%d\n%d" %(x, y, z))
