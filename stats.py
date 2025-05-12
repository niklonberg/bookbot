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
  
  print("--------- Character Count -------")
  for c in char_list:
    print(f"{c['char']}: {c['count']}")