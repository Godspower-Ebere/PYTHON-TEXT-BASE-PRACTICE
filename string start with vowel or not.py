while True:
    string=(input("ENTER A WORD PLEASE: ".title())).lower()
    if string[0]=='a' or string[0]=='e' or string[0]=='i' or string[0]=='o' or string[0]=='u':
        print(string.title() + " START WITH a VOWEL".title())

    elif:
        print(string.title() + " START WITH a CONSONANT".title())
    else:
        print("please type a word correctly".title())
