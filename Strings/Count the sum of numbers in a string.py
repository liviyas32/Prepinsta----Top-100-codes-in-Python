import re

def numsum(z):

  pattern = r'[\d+]'

  numbers = sum(map(int,re.findall(pattern,z)))

  return numbers

chr = input("Enter a string : ")
numsum(chr) 

#other way
sum = 0
for i in range(len(z)):
  if z[i].isdigit() == True:
    sum += int(z[i])
print(sum)
