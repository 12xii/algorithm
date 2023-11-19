while True:
  try:
      a, b = input().split()
      print(int(b) // (int(a) + 1))
  except EOFError:
      break