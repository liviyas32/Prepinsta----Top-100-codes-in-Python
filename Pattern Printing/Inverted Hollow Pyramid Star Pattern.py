rows = int(input("Enter a number : "))

for i in range(rows-1,-1,-1): #3,2,1,0
  for j in range(rows-i): #0,1,2,3
    print(" ", end = ' ')
  for j in range(i*2+1): #7,5,3,1
    if (j in range(1,i*2)) & (i in range(1, rows-1)): #(1-6) & (1-2) ...
      print(" ", end = ' ')
    else:
      print("*", end = ' ')
  print()
