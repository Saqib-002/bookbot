from stats import get_words, get_characters, print_report
import sys

def get_book_text(path):
    with open(path) as f:
        file_contents=f.read()
    return file_contents


def main():
    args=sys.argv
    if len(args)<=1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    content=get_book_text(args[1])
    num_words=get_words(content)
    print(f"{num_words} words found in the document")
    char_count=get_characters(content)
    print_report(num_words,char_count)

main()
