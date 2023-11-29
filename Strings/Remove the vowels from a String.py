def remove_vowels(t):
  vowels = ['a','e','i','o','u']
  t = t.lower()

  new_word = ''
  for i in range(len(t)):
    if t[i] not in vowels:
      new_word += t[i]

  return new_word

tar = input("Enter a string : ")

remove_vowels(tar)
