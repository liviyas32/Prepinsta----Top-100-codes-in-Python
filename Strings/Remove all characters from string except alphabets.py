def alpha(s):
  only_alpha = ''
  
  for i in range(len(s)):
    if ((ord(s[i])>=65) and (ord(s[i])<=90) or ((ord(s[i])>=97) and (ord(s[i])<=122))):
      only_alpha += s[i]

  return only_alpha

ch = input("Enter a string : ")
alpha(ch)
