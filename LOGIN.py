import random
import datetime
import time
from datetime import date
while True:
    x=random.randint(0,9)

    x1=random.randint(0,9)

    x2=random.randint(0,9)

    x3=random.randint(0,9)
    print()
    print()
    print("          hello welcome to my game".title())
    time.sleep(2)
    print("hi your password is".title(),x,x1,x2,x3)
    time.sleep(5)
    
    print()
    password=input("please enter your password to login: ".title()).strip()
    if password[0]==str(x) and password[1]==str(x1) and password[2]==str(x2) and password[3]==str(x3):
        print("hello you are welcome".title())
        print("do you want to know todays date?".title())
        print("ask me what is todays date".title())
        today=input("ask: ".title())
        now=datetime.datetime.today()
        now=now.strftime("%d %B  %Y")
        if "date" in today:
            print("todays date is".title(),now)
    elif password.isspace:
        print("incorrect password !!!".title())    
    else:
        print("incorrect password !!!".title())
    
