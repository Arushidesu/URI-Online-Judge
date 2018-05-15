A, B, C = input().split(" ")
A, B, C = float(A), float(B), float(C)
delta = (B ** 2) - (4 * A * C)
if delta < 0 or A == 0:
    print("Impossivel calcular")
else:
    R1 = "%.5f" % (((-1 * B) + (delta ** 0.5)) / (2 * A))
    R2 = "%.5f" % (((-1 * B) - (delta ** 0.5)) / (2 * A))
    print("R1 = %s\n"
          "R2 = %s" %(R1, R2))
