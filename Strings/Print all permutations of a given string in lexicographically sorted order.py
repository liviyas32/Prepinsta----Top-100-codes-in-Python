values = []

def permutation(string, ini, len):
  if ini == len:
    values.append("".join(string))
  else:
    for i in range(ini, len):
      string[ini], string[i] = string[i], string[ini]
      permutation(string, ini+1, len)
      string[ini], string[i] = string[i], string[ini]
  
  
 

string = input("Enter a string : ")
initial = 0
length = len(string)

permutation(list(string), initial, length)
for value in sorted(values):
  print(value)
