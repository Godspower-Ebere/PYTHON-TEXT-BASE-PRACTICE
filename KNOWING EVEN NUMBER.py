import time
while True:
    
    print("      do you want to know even number!!!".title())
    answer=input("enter a number to get the even number: ".title()).strip()
    if answer.isalpha():
        print("'please i want you to enter a number'".title())
    else:
        answer=int(answer)
        if answer % 2 == 0:
            for i in range(0 ,answer,2):
                print(i)
            print(answer)
        elif answer % 2 == 1:
            print(answer,"is an odd number".title())
            print("but this are the even number in".title(),answer)
            answer-=1
            print("processing...".title())
            time.sleep(5)
            if answer % 2 == 0:
                answer+=2
                for i in range(0,answer,2):
                    print(i)
