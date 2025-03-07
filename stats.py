def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()

def get_book_wc(text):
  return len(text.split())

def character_count(text):
  count_dict = {}
  for char in text:
    if char.lower() in count_dict:
      count_dict[char.lower()] += 1
    else:
      count_dict[char.lower()] = 1
  return count_dict

def sort_on(dict):
  return dict["count"]

def sorted_count(dict):
  char_list = []
  for char, count in dict.items():
    char_dict = {"char": char, "count": count}
    char_list.append(char_dict)

  char_list.sort(reverse=True, key=sort_on)
  return char_list
