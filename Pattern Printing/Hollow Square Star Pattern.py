rows = int(input("Enter number of rows : "))
cols = rows

for i in range(rows):
  for j in range(cols):
    if (j in range(1,cols-1)) & (i in range(1,rows-1)):
      print(" ", end = ' ')
    else:
      print("*", end = ' ')
  print()
