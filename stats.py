def word_count(text):
  words = text.split()
  number_of_words = len(words)
  return number_of_words
  

def count_characters(text):
  result = {}
  for char in text:
    lower_char = char.lower()
    if lower_char in result:
      result[lower_char] += 1
    else:
      result[lower_char] = 1
  return result

def sort_on(items):
  return items["num"]

def sort_counted_characters(counted_characters):
  l = []
  for k in counted_characters:
    if k.isalpha():
      l.append({"char": k, "num": counted_characters[k]})
  l.sort(key=sort_on, reverse=True)
  return l
  

