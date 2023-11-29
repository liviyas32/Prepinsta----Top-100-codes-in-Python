def character(c):
  vowels = ['a','e','i','o','u']

  c = c.lower()
  
  if c in vowels:
    return "vowel"
  else:
    return "consonant"

ch = input("Enter a character : ")
character(ch)
