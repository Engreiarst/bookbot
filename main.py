# python
import stats
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path = sys.argv[1]
# use `path` instead of any hard-coded "books/....txt"

REPORT_HEADER = f"""============ BOOKBOT ============
Analyzing book found at ... {path}
----------- Word Count ----------"""

REPORT_CHAR_HEADER = "--------- Character Count -------"
REPORT_FOOTER = "============= END ==============="

def get_book_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def format_char_lines(char_counts):
    sorted_chars = stats.sort_characters(char_counts)
    return "\n".join(
        f"{item['char']}: {item['num']}"
        for item in sorted_chars
        if item["char"].isalpha()
    )

def main():
    book_text = get_book_text(path)
    total_words = stats.get_num_words(book_text)
    char_counts = stats.get_num_characters(book_text)
    char_lines = format_char_lines(char_counts)

    print(
        f"{REPORT_HEADER}\n"
        f"Found {total_words} total words\n"
        f"{REPORT_CHAR_HEADER}\n"
        f"{char_lines}\n"
        f"{REPORT_FOOTER}"
    )

if __name__ == "__main__":
    main()