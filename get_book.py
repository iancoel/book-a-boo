import os
import requests

from consts import BOOK_PATH, BOOKS_DIR_PATH

url = "https://raw.githubusercontent.com/asweigart/codebreaker/master/frankenstein.txt"

def get_book():
  if not should_download():
    return

  check_dir_exists()

  response = requests.get(url)

  if response.status_code == 200:
      with open(BOOK_PATH, "wb") as file:
          file.write(response.content)
      print("Saved book file")
      print("")
  else:
      print(f"Request failed: {response.status_code}")

def should_download():
  if os.path.exists(BOOK_PATH):
    print(f"File {BOOK_PATH} has already been downloaded.")
    print("")
    return False

  return True

def check_dir_exists():
  if not os.path.exists(BOOKS_DIR_PATH):
    os.makedirs(BOOKS_DIR_PATH)
