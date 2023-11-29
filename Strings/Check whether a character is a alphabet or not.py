def isalphabet(ch):
  if ((ord(ch) >= 65) and (ord(ch) <=90)) or ((ord(ch) >=97) and (ord(ch) <=122)):
    is_alpha = True
  else:
    is_alpha = False

  return is_alpha

c = input("Enter a character : ")

isalphabet(c)

#using builtin function
c.isalpha()
