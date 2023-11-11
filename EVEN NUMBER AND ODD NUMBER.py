while True:
    number=input("ENTER A NUMBER PLEASE: ").strip()
    if number.isdigit():
        number=int(number)
        if number % 2 == 0:
            print(number,"is an 'EVEN' number ")
        elif number % 2 == 1:
            print(number,"is a 'ODD' number")
        elif number.isalnum:
            print("please type a number!!!".title())
        elif number.strip:
            print("you didnt type anything!!!".title())
    else:
        print("Type a number please ...")
