#python
def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text="books/frankenstein.txt"):
    lowered = text.lower()
    uniques = set()
    character_count = dict()
    for char in lowered:
        uniques.add(char)
        character_count[char] = lowered.count(char)
    return character_count

def sort_characters(character_count):
    sorted_characters = sorted(character_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_characters.isalpha()