rows = int(input("Enter row number : "))

for i in range(rows,0,-1):
  for j in range(i-1):
    print(" ", end = ' ')
  for j in range(rows):
    print("*", end = ' ')
  print()
