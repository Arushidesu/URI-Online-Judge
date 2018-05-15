A, B, C = map(float, input().split())
if (abs(B - C) < A < (B + C)) and (abs(A - C) < B < (A + C)) and (abs(A - B) < C < (A + B)):
    perimetro = ("%.1f" % (A + B + C))
    print("Perimetro = %s" %perimetro)
else:
    area = "%.1f" % (C * (A + B) / 2)
    print("Area = %s" %area)
