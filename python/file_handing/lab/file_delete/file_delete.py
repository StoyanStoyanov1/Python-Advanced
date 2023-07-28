import os

try:
    os.remove("my first_file.txt")
except FileNotFoundError:
    print("File already deleted!")