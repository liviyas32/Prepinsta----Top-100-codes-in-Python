def ismatch(a, b):
  n = len(a)
  m = len(b)

  if n==0 and m==0:
    return True
  elif n>1 and a[0]=='*' and m==0:
    return False
  elif (n>1 and a[0] == '?') or (n!=0 and m!=0 and a[0] == b[0]):
    return ismatch(a[1:], b[1:])
  elif (n>1 and a[0] == '*') and m!=0:
    return ismatch(a[1:], b) or ismatch(a, b[1:])

s1 = input("Enter first string with wild character : ")
s2 = input("Enter second string : ")

ismatch(s1,s2)
