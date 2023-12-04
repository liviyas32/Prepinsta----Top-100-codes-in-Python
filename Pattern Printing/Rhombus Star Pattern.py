rows = int(input("Enter number of rows : "))
cols = rows

for i in range(rows):
  for j in range(i+1):
    print(" ", end = ' ')
  for j in range(cols):
    print("*", end = ' ')
  print()
