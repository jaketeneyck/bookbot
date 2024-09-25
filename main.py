def main():
    with open("books/frankenstein.txt") as f:
        contents = f.read()
    #print(contents)
    #print(count_words(contents))
    print(count_chars(contents))

def count_words(s):
    count = 0
    words = s.split()

    for word in words:
        count += 1
    
    return count

def count_chars(s):
    # keys for checking that we want the given char
    keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    # convert string to all lower case and create list of chars
    s = s.lower()
    chars = list(s)
    clean_chars = []
    
    for c in chars:
        # remove whitespace chars
        if c in keys:
            clean_chars.append(c)


    # create dictionary for holding letter counts
    char_count = {}
    
    for k in keys:
        char_count[k] = 0


    # count chars and update dictionary 
    for c in clean_chars:
        char_count[c] += 1

    return char_count

main()