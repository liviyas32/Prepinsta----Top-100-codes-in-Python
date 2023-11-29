def capitalize(string):
  fullstring = ""
  for word in string.split():
    modified = word[0:1].upper()+word[1:len(word)-1]+word[-1:].upper()
    fullstring =fullstring +" "+modified
  return fullstring

chr = input("Enter a string : ")
capitalize(chr)
