def main():
    count_words(get_book_text("books/frankenstein.txt"))

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def count_words(text):
    num_words = len(text.split())
    print(num_words, "words found in the document")

main()