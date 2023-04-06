#question5

def reverse_words(s):
    l = (s.split())[::-1]
    result = str()
    for i in l:
        result += i + " "
    return result[:-1]
    
if __name__ == "__main__":
    s = "Two roads diverged in a yellow wood, And sorry I could not travel both And be one traveler, long I stood And looked down one as far as I could To where it bent in the undergrowth;"
    print("s: ")
    print(s)
    print()
    print("reversed: ")
    print(reverse_words(s))
    print()
    print()
    s = "Then took the other, as just as fair, And having perhaps the better claim, Because it was grassy and wanted wear; Though as for that the passing there Had worn them really about the same,"
    print("s: ")
    print(s)
    print()
    print("reversed: ")
    print(reverse_words(s))
    print()
    print()
