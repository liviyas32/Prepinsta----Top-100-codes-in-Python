rows = int(input("Enter number of rows for square star pattern : "))
cols = rows

for i in range(rows):
  for j in range(cols):
    print("*", end = ' ')
  print()
