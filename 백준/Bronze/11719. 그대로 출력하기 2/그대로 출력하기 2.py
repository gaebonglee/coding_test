for i in range(100):
  try:
    text = input()
    print(text)
  except EOFError:
    break