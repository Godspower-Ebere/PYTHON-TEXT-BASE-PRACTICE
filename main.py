print("                WELCOME TO MY QUIZ GAME!")

name=input("WHAT IS YOUR NAME? ")
age=input(name.upper() + " HOW OLD ARE YOU? ")
try:
    number=int(age)
except:
    print("                 INVALID AGE")
    quit()
if float(age) < 15:
    print(name + " YOU ARE NOT OLD ENOUGH TO PLAY THIS GAME!")
    quit()
else:
    print("               OKAY LETS PLAY!")
        
score=0
incorrect=0
complete=7

ques=input("HOW MANY STATE DO WE HAVE IN NIGERIA? ")
if ques == "36":
    print("CORRECT")
    score+=1
else:
    print("INCORRECT")
    incorrect+=1
 
ques=input("HOW OLD IS GODSPOWER? ")
if ques == "15":
    print("CORRECT")
    score+=1
else:
    print("INCORRECT")
    incorrect+=1
        
abu=input("WHAT IS THE CAPITAL OF NIGERIA? ")
if abu != "abuja" :
    print("INCORRECT")
    incorrect+=1
else:
    print('CORRECT')
    score+=1
        
ques=input("HOW MANY STATE DO WE HAVE IN NIGERIA? ")
if ques == "36":
    print("CORRECT")
    score+=1
else:
    print("INCORRECT")
    incorrect+=1
        
ques=input("HOW MANY STATE DO WE HAVE IN NIGERIA? ")
if ques == "36":
    print("CORRECT")
    score+=1
else:
    print("INCORRECT")
    incorrect+=1
        
ques=input("2  x  2 = ? ")
if float(ques) == 4:
    print("CORRECT")
    score+=1
else:
    print("INCORRECT")
    incorrect+=1
    
        
ques=input("HOW OLD IS MY DAD? ")
if ques == "58":
    print("CORRECT")
    score+=1
else:
    print("INCORRECT")
    incorrect+=1
    
print("YOU GOT " + str(score) +  " OUT OF " + str(complete) + " QUESTION CORRECT")

print("AND YOU GOT " + str(incorrect) + " QUESTION INCORRECT")        
 
