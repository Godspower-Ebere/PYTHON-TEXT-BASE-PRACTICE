from pdf2docx import Converter
import time
print("PDF TO WORD CONVERTER BY GP")
while True:
    ask=input("What do you want? ".title()).lower().strip()
    if ask[0]=="c":
        print("Okay")
    else:
        print("Follow my procedure bye.........".title())
        time.sleep(2)
        break
    pdf=input("what is the name of the file? ".title()).strip()
    if ".pdf" in pdf:
        print("okay".title())
    else:
        print("You are not okay Follow my procedure bye......... ".title())
        break
    word=input("which format do you want it? ".title()).strip()
    if ".docx" in word:
        print("okay".title())
        print("In progress....")
        time.sleep(2)
    else:
        print("that is not the file you want to convert".title())
        time.sleep(2)
        break
    cv=Converter(pdf)
    covert=cv.convert(word)
    print(pdf,"converted to word document".title(),"successfuly".title())
    print("Goodbye")
    time.sleep(3)
