t = int(input())
for i in range(t):
    bd = bg = 0
    b = int(input())
    ad, dd, ld = map(int, input().split())
    ag, dg, lg = map(int, input().split())
    if ld % 2 == 0:
        bd = b
    if lg % 2 == 0:
        bg = b
    vd = ((ad + dd) / 2) + bd
    vg = ((ag + dg) / 2) + bg
    if vd > vg:
        print("Dabriel")
    elif vg > vd:
        print("Guarte")
    else:
        print("Empate")
