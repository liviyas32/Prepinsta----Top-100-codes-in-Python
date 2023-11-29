def nonrepeating(s):
  word_dict = {}

  for i in sorted(s.lower()):
    if i not in word_dict:
      word_dict[i] = 1
    else:
      word_dict[i] += 1
  
  for i,j in word_dict.items():
    if j<2:
      print(i)

e = input("Enter a string : ")
nonrepeating(e)
