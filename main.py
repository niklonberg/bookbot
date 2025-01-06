def main():
  with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    print(f"{count_words(file_contents)} words found in document")
    characters_dict = get_characters_count(file_contents)
    print_alphabet_characters(characters_dict)
    print("- End of report -")
  
def count_words(text):
  words = text.split()
  return len(words)

def get_characters_count(text):
  character_counts = {}
  for c in text:
    lowercased = c.lower()
    if (lowercased in character_counts):
      character_counts[lowercased] += 1
    else:
      character_counts[lowercased] = 1
  
  return character_counts

def print_alphabet_characters(character_dict):
  char_list = []
  for c in character_dict:
    if (c.isalpha()):
      char_list.append({
        "char": c,
        "count": character_dict[c]
        })
      
  def sort_on(dict):
    return dict["count"]
  
  char_list.sort(reverse=True, key=sort_on)
  
  for c in char_list:
    print(f"The '{c['char']}' character was found '{c['count']}' times.")

main()
