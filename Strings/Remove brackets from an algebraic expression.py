def remove_brackets(x):
  brackets = ["(",")","{","}","[","]"]
  new_string = ''

  for i in range(len(x)):
    if x[i] not in brackets:
      new_string += x[i]

  return new_string

chr = input("Enter an expression : ")
remove_brackets(chr)
