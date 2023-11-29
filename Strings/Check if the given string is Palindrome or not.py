def ispalindrome(f):
  is_palindrome = False
  reversed = f[::-1]

  if f == reversed:
    is_palindrome = True

  return is_palindrome
  
df = input("Enter a string : ")
ispalindrome(df)
