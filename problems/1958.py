N = float(input())
if N < 0:
    print("%.4E" %N)
elif N > 0:
    print("+%.4E" %N)
else:
    string = str(N)
    if string == '-0.0':
        print("%.4E" % N)
    else:
        print("+%.4E" % N)
