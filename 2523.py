while True:
  try:
    a = input()
    input()
    v = map(int, input().split())
    for i in v:
      print(a[i-1], end='')
    print()
  except EOFError:
    break
