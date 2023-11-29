def countsequence(a,b):
  matrix = [[0 for i in range(len(b)+1)] for i in range(len(a)+1)]
  n, m = len(a), len(b)

  for i in range(n+1):
    for j in range(m+1):
      if a[i-1] == b[j-1]:
        matrix[i][j] = 1 + matrix[i-1][j] + matrix[i][j-1]
      else:
        matrix[i][j] = 1 + matrix[i-1][j] + matrix[i][j-1] - matrix[i-1][j-1]
  
  return matrix[n][m]

s1= input("Enter a string : ")
s2 = input("Enter a sub-string : ")

countsequence(s1.upper(),s2.upper())
