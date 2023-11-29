#builtin function
S = "geeksforgeeks"
S1 = "eek"
S2 = "ok"
S.replace(S1,S2)

#using traversal
def replace(main, sub, new):
  final = ''

  i = 0
  while i < len(main):
    k = 0
    if main[i] == sub[k] and i+len(sub) <= len(main):
      j = i

      while j < i+len(sub) and main[j] == sub[k]:
        j += 1
        k += 1
      
      if j == i+len(sub):
        final += new
        i = j-1

      else:
        final += main[i]
    else:
      final += main[i]
    i += 1

  return final

string = input("Enter a string : ")
sub_string = input("Enter a sub-string : ")
new_word = input("Enter a new word to insert : ")

replace(string, sub_string, new_word)
