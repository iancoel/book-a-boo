from consts import BOOK_PATH
from get_book import get_book

def main():
  get_book()

  with open(BOOK_PATH) as file:
    complete_file = file.read()
    word_count = len(complete_file.split())
    letter_count = {}

    for letter in complete_file:
      normalized_letter = letter.lower()
      count = letter_count.get(normalized_letter)

      if not normalized_letter.isalpha():
        continue

      if count:
        letter_count[normalized_letter] += 1
      else:
        letter_count[normalized_letter] = 1

    sorted_letter_count = sort_dict(letter_count)

    print(f"=== {BOOK_PATH} report ===")
    print(f"{word_count} found")
    print("")

    for key in sorted_letter_count:
      print(f"The '{key}' character was found {sorted_letter_count[key]} times")

    print("=== End report ===")

def sort_dict(dict):
  sorted_keys = sorted(dict, key=lambda k: dict[k], reverse=True)
  return {key: dict[key] for key in sorted_keys}

if __name__ == "__main__":
  main()