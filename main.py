from stats import get_num_words

def get_book_text(path="books/frankenstein.txt"):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    count = get_num_words(book_text)
    print(f"{count} words found in the document")

if __name__ == "__main__":
    main()