def reverse(p):
  reversed = ''

  for i in range(len(p)):
    reversed = p[i]+reversed

  return reversed

g = input("Enter a string : ")
reverse(g)
