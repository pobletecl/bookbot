def count_words(text):
    num_words = len(text.split())
    print(num_words, "words found in the document")

def count_characters(text):
    char_dict = dict.fromkeys(list(text.lower()))
    for char in text.lower():
        if char_dict[char] == None:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    
    print(char_dict)
    

