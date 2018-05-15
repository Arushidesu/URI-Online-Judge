A, B, C, D = map(int, input().split())
if (abs(B - C) < A < B + C and abs(A - C) < B < A + C and abs(B - A) < C < B + A) or (abs(B - D) < A < B + D and abs(A - D) < B < A + D and abs(B - A) < D < B + A) or (abs(D - C) < A < D + C and abs(A - C) < D < A + C and abs(D - A) < C < D + A) or (abs(B - C) < D < B + C and abs(D - C) < B < D + C and abs(B - D) < C < B + D):
    print("S")
else:
    print("N")
