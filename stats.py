#python
def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text="Text"):
    lowered = text.lower()
    uniques = set()
    character_count = dict()
    for char in lowered:
        uniques.add(char)
        character_count[char] = lowered.count(char)
    return character_count