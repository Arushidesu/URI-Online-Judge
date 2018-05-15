A, B, C = map(int, input().split())
if B < A and (C > B or B == C):
    print(":)")
if B > A and (C < B or B == C):
    print(":(")
if B > A and C > B and C - B < B - A:
    print(":(")
if B > A and C > B and C - B >= B - A:
    print(":)")
if A > B and B > C and A - B > B - C:
    print(":)")
if A > B and B > C and A - B <= B - C:
    print(":(")
if A == B:
    if C > B:
        print(":)")
    else:
        print(":(")
