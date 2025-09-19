import sys

from stats import word_count, count_characters,sort_counted_characters

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
  if(len(sys.argv) != 2):
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)

  file_path = sys.argv[1]

  book_text = get_book_text(file_path)
  number_of_words = word_count(book_text)
  counted_characters = count_characters(book_text)
  sorted_list = sort_counted_characters(counted_characters)

  print('============ BOOKBOT ============')
  print(f'Analyzing book found at books/frankenstein.txt...')
  print('----------- Word Count ----------')
  print(f'Found {number_of_words} total words')
  print('------- Character Count --------')
  for item in sorted_list:
      print(f'{item["char"]}: {item["num"]}')
  print('============= END ===============')

main()
