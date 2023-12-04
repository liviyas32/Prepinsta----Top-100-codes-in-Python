rows = int(input("Enter a number : ")) #6

for i in range(rows): #0,1,2,3,4,5
  for j in range(i+1): #1,2,3,4,5,6
    print("*", end = ' ')
  print()

for i in range(rows-1): #0,1,2,3,4
  for j in range(rows-i-1): #5,4,3,2,1
    print("*", end = ' ')
  print()
