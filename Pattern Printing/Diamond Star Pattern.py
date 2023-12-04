rows = int(input("Enter a number : ")) #4

for i in range(rows): #0,1,2,3
  for j in range(rows-i-1): #3,2,1,0
    print(" ", end = ' ')
  for j in range(i*2+1): #1,3,5,7
    print("*", end = ' ')
  print()

for i in range(rows-2,-1,-1): #2,1,0
  for j in range(rows-i-1): #1,2,3
    print(" ", end = ' ')
  for j in range(i*2+1): #5,3,1
    print("*", end = ' ')
  print()
