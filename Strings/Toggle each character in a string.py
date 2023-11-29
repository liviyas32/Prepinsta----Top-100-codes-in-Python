def toggle(f):

  toggled_case = ""

  for i in range(len(f)):
    if f[i].isupper() == True:
      toggled_case = toggled_case+f[i].lower()
    else:
      toggled_case = toggled_case+f[i].upper()
  
  return toggled_case

char = input("Enter a character : ")
toggle(char)

#builtin function
char.swapcase()
