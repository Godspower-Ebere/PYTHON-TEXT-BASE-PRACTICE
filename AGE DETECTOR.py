while True:
    print("              HI WELCOME TO MY AGE DETECTOR!".title())
    name=input("HELLO WHAT IS YOUR NAME? ".title()).strip().upper()
    ans=input(name+ " TYPE YOUR BIRTH YEAR: ".title())
    try:
        number=int(ans)
    except:
        print("INVALID BIRTH YEAR!!!")
    ans=int(2023)-int(number)
    print(str(name).title() + " YOU ARE ".title() + str(ans).title() + " YEARS OLD.".title())
