rows = int(input("Enter a number : "))

for i in range(rows): #0,1,2,3
  for j in range(rows-i-1): #3,2,1,0
    print(" ", end = ' ')
  for j in range(i*2+1): #1,3,5,7
    if (j in range(1, i*2)) & (i in range(1, rows-1)): 
      print(" ", end = ' ')
    else:
      print('*', end = ' ')
  print()
