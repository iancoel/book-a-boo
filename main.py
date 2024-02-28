def main():
  book_path = "books/frankenstein.txt"

  with open(book_path) as file:
    complete_file = file.read()
    letter_count = {}

    for letter in complete_file:
      normalized_letter = letter.lower()
      count = letter_count.get(normalized_letter)
      if count:
        letter_count[normalized_letter] += 1
      else:
        letter_count[normalized_letter] = 1

    print(letter_count)

if __name__ == "__main__":
  main()