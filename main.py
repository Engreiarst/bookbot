#moved to WSL: Ubuntu from Windows pathway
import stats

def get_book_text(path="books/frankenstein.txt"):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    count = stats.get_num_words(book_text)
    character_numbers = stats.get_num_characters(book_text)
    print(f"{count} words found in the document", character_numbers)

if __name__ == "__main__":
    main()