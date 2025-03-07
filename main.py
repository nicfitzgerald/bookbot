import sys
from stats import get_book_text, get_book_wc, character_count, sorted_count

book_path = ""
if len(sys.argv) < 2:
  print("Usage: python3 main.py <path_to_book>")
  sys.exit(1)
else:
  book_path = sys.argv[1]

book_text = get_book_text(book_path)

def main():
  word_count = get_book_wc(book_text)
  char_count = character_count(book_text)
  sort_count = sorted_count(char_count)

  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {book_path}...")
  print("----------- Word Count ----------")
  print(f"Found {word_count} total words")
  print("--------- Character Count -------")
  for item in sort_count:
    if item['char'].isalpha():
      print(f"{item['char']}: {item['count']}")
  print("============= END ===============")

main()