print()
name=print("   hi my name is godpspower".title())
while True:
    my_name=input("enter a name please: ".title()).lower().strip()
    if my_name.isdigit():
        print("please type a name".title())
    else:
        if my_name=="n" or my_name[:2]=="ju" or my_name[:2]=="bl" or my_name[:4]=="chid" or my_name[0]=="n" or my_name[:4]=="chia" or my_name[:2]=="di" or my_name[:2]=="es" or my_name[0]== "g"  or my_name[:4]=="chik" or my_name[:]== "chia" or my_name[:2]== "am" or my_name[:2]=="pre":
            print(my_name.title(),"is a girl".title())
            print()
        elif my_name[:5]=="chidi" or my_name[:4]=="chin" or my_name[:2]=="da" or my_name[:2]=="do" or my_name[0]=="e" or my_name[0]=="m" or my_name[0]=="j" or my_name[:3]=="god" or my_name[:2]=="ak" or my_name[:2]=='pa':
            print(my_name.title(),"is a boy".title())
            print()
        else:
            print(my_name.title(),"is either a girl or  a boy".title())
