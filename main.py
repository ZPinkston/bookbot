def main():
    with open("/home/pinkiepi/workspace/github.com/ZPinkston/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)
    word_count = count_words(file_contents)
    print(f"----Print Report-----")
    print(f"Total words: {word_count}")
    sorted_counts = count_letters(file_contents)
    # print(f"Sorted letter counts: {sorted_counts}")
    letter_count_print(sorted_counts)
    print(f"-----End Report-----")

def count_words(file_contents):
    words = file_contents.split()
    
    return len(words)

def count_letters(file_contents):
    letter_count = {}
    for letter in file_contents:
        if letter.isalpha():
            letter = letter.lower()
            letter_count[letter] = letter_count.get(letter, 0) + 1
        sorted_letter_counts = dict(sorted(letter_count.items()))

    return sorted_letter_counts

def letter_count_print(letter_counts):
    for letter, count in letter_counts.items():
        print(f"The letter {letter} was found in the document {count} times.")
    

main()