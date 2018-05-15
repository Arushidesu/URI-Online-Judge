x = float(input())
v100 = 1000 * 0.08
v150 = 1500 * 0.18
if 0 <= x <= 2000:
    print("Isento")
elif 2000 <= x <= 3000:
    vr = x - 2000
    ir = "%.2f" % (vr * 0.08)
    print("R$ %s" %ir)
elif 3000 <= x <= 4500:
    vr = x - 3000
    vf = "%.2f" % (v100 + (vr * 0.18))
    print("R$ %s" %vf)
elif x > 4500:
    vr = x - 4500
    vf = "%.2f" % (v150 + v100 + (vr * 0.28))
    print("R$ %s" %vf)
