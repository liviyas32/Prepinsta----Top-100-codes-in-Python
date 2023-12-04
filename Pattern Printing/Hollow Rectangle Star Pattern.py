rows = int(input("Enter a number : "))
cols = int(input("Enter a number : "))

for r in range(rows):
  for c in range(cols):
    if (r in range(1,rows-1)) & (c in range(1, cols-1)):
      print(" ", end = ' ')
    else:
      print("*", end = ' ')
  print()
