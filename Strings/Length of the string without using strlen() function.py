def length(g):
  g_list = sorted(g)

  count = 0
  for i in g_list:
    count += 1

  return count

var = input("Enter a character : ")
length(var)
