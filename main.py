def main():
  book_path = "books/frankenstein.txt"

  with open(book_path) as file:
    complete_file = file.read()
    complete_file_splitted = complete_file.split()
    print(len(complete_file_splitted))

if __name__ == "__main__":
  main()