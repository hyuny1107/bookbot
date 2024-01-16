def main():
    book_path = "books/frankenstein.txt"
    report(book_path)

    


def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    words = text.split()
    return len(words)

def letter_count(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def report(path):
    print(f"--- Begin report of {path} ---")

    text = get_book_text(path)

    num_words = word_count(text)
    print(f"{num_words} words found in the document")

    num_letters = letter_count(text)
    letter_list = list(num_letters.items())
    letter_list.sort()

    for c in letter_list:
        if c[0].isalpha():
           print(f"The '{c[0]}' character was found {c[1]} times")
    
    return None

    
main()