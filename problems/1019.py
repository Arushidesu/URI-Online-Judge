seg = int(input())
min = hor = 0;
while(seg >= 60):
    min += 1
    seg -= 60
while(min >= 60):
    hor += 1
    min -= 60
print("%d:%d:%d" %(hor, min, seg))
