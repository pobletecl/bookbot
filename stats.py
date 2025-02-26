def count_words(text):
    num_words = len(text.split())
    print("----------- Word Count ----------")
    print("Found", num_words, "total words")

def count_characters(text):
    print("--------- Character Count -------")
    char_dict = dict.fromkeys(list(text.lower()))

    for char in text.lower():
        if char_dict[char] == None:
            char_dict[char] = 1
            
        else:
            char_dict[char] += 1
    del char_dict[" "]
    sorted_list = {key: val for key, val in sorted(char_dict.items(), key = lambda ele: ele[1], reverse = True)}
    for key in sorted_list:
        print(key + ": " + str(sorted_list[key]))

    print("============= END ===============")