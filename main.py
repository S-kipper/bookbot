from stats import num_of_words, char_appears, sort_on
import sys
#print(sys.argv)
if(len(sys.argv) != 2):
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath, encoding="utf-8") as f:
        return f.read()

def main():
    #filepath = input()
    book_text = get_book_text(sys.argv[1])
    num_words = num_of_words(book_text)
    char_appearance = char_appears(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in char_appearance:
        print(f"{item['char']}: {item['count']}")
    print("============= END ===============")


main()
