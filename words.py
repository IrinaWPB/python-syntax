def print_upper_words(list, start_with=['e', 'g']):
    for word in list:
        for letter in start_with:
            if word[0].upper() == letter.upper():
                print(word.upper())