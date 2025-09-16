#python
def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    lowered = text.lower()
    counts = {}
    for ch in lowered:
        counts[ch] = counts.get(ch, 0) + 1
    return counts

# python
def sort_characters(character_count):
    letters_only = {ch: c for ch, c in character_count.items() if str(ch).isalpha()}
    top = sorted(letters_only.items(), key=lambda kv: kv[1], reverse=True)
    return [{"char": ch, "num": cnt} for ch, cnt in top]