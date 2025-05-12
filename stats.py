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