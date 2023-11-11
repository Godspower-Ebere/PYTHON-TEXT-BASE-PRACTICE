import random
guesstaken=0
myname=input("hello ! what is your name? ".title())
number=random.randint(1,20)
print("well".title(),myname,"i am thinking of a number between 1 and 20")
while guesstaken < 6:
    guess=input("Take A Guess: ")
    guess=int(guess)
    guesstaken+=1
    if guess < number:
        print("your guess is too low".title())
    elif guess > number:
        print("your guess is too high".title())
    elif guess == number:
        break
if guess == number:
    guesstaken=str(guesstaken)
    
    print("good job !".title(),myname.title(),"you guessed my number in".title(),guesstaken,"guesses".title())
elif guess != number:
    print('nope the number i was thinking of was'.title(),number)
