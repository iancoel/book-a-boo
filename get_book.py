import os
import requests

file_path = "books/frankenstein.txt"

url = "https://raw.githubusercontent.com/asweigart/codebreaker/master/frankenstein.txt"
dir_path = "books"

def get_book():
  if not should_download():
    return

  check_dir_exists()

  response = requests.get(url)

  if response.status_code == 200:
      with open(file_path, "wb") as file:
          file.write(response.content)
      print("Saved book file")
      print("")
  else:
      print(f"Request failed: {response.status_code}")

def should_download():
  if os.path.exists(file_path):
    print(f"File {file_path} has already been downloaded.")
    print("")
    return False

  return True

def check_dir_exists():
  if not os.path.exists(dir_path):
    os.makedirs(dir_path)
