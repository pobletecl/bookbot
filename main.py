from stats import count_words
from stats import count_characters
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    elif len(sys.argv) == 2:
        print("============ BOOKBOT ============")
        print("Analyzing book found at " + str(sys.argv[1]) + "...")
        count_words(get_book_text(sys.argv[1]))
        count_characters(get_book_text(sys.argv[1]))

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

main()