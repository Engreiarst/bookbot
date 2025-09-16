# python
#def get_num_words(text):
#    words = text.split()
#    return len(words)

def get_num_characters(text="books/frankenstein.txt"):
    uniques = set(text)
    character_count = dict()
    for char in uniques:
        character_count[char] = text.count(char)
    print(character_count)