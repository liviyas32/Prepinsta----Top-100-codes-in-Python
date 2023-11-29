def replaceword(s, sub, new):
  final = ''

  i = 0
  while i<len(s):
    k=0
    if s[i] == sub[k] and i+len(sub) <= len(s):
      j = i
      while j < i+len(sub) and s[j] == sub[k]:
        j += 1
        k += 1
      if j == i+len(sub):
        final += new
        i = j-1
      else:
        final += s[i]
    else:
      final += s[i]

    i += 1

  return final


string = input("Enter a string : ")
sub_string = input("Enter a sub-string : ")
new_word = input("Enter a new word to insert : ")

replace(string, sub_string, new_word)

# builtin
string.replace(sub_string, new_word)
