from stats import count_words, get_characters_count, print_alphabet_characters

def main():
  with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(file_contents)} total words")
    characters_dict = get_characters_count(file_contents)
    print_alphabet_characters(characters_dict)
    print("- End of report -")

main()
