def get_words(text):
    return len(text.split())

def get_characters(text):
    char_count={}
    for t in text:
        l=t.lower()
        if l in char_count:
            char_count[l]+=1
            continue
        char_count[l]=1
    return char_count

def print_report(wc,count):
    count= dict(sorted(count.items(),key=lambda i: i[-1],reverse=True))
    print("""
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
         """)
    print(f"Found {wc} total words")
    print("--------- Character Count -------")
    for c in count:
       print(f"{c}: {count[c]}")
    print("============= END ===============")
