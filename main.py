import sys

from stats import count_words, get_characters_count, print_alphabet_characters

def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  book_path = sys.argv[1]

  with open(book_path) as f:
    file_contents = f.read()
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(file_contents)} total words")
    characters_dict = get_characters_count(file_contents)
    print_alphabet_characters(characters_dict)
    print("- End of report -")

main()
