from stats import count_words
from stats import count_characters

def main():
    count_words(get_book_text("books/frankenstein.txt"))
    count_characters(get_book_text("books/frankenstein.txt"))

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

main()