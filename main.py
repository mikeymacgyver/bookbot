book_path = "books/frankenstein.txt"


def main():
    

    with open(book_path) as f:
        book_contents = f.read()
        charCount(book_contents)


def get_num_words(text):
    words = text.split()
    return len(words)

def sort_on(charCount):
    return charCount[num]


def charCount(book_contents):
    charCount = {}
    lowerChar = book_contents.lower()
    num_words = get_num_words(book_contents)
    for character in lowerChar:
        if character in charCount:
            charCount[character] += 1
        else:
            charCount[character] = 1
    
    #Sort the Dictionary now by converting to list
    sortedCharCount = dict(sorted(charCount.items(), key=lambda item: item[1], reverse=True))
    charCount = sortedCharCount

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for character in charCount:
            charNum = charCount[character]
            if character.isalpha() and character != " ":
                print(f"The '{character}' character was found {charNum} times")

    print("--- End report ---")

    #return charCount


main()