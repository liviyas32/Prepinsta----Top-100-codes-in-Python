rows = int(input("Enter row number : "))
cols = int(input("Enter column number : "))

for r in range(rows):
  for c in range(r+1):
    print(" ", end = ' ')
  for c in range(cols):
    print("*", end = ' ')
  print()  
