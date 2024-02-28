def main():
  book_path = "books/frankenstein.txt"

  with open(book_path) as file:
    print(file.read())

if __name__ == "__main__":
  main()