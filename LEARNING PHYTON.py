for x in range(3):
    print("hello world")
i=0

while i < 5:
    print(i)
    i+=1
text ="hello"
for txt in text:
    if txt== "l":
        continue
    print(txt)
class person:
    first="godspower"
    last="ebere"
    age="15"
man=person()
print(man.first)

x="i love {} very much"
text=x.format("phyton")
print(text)
x="i love {0} , {2} and {1} very much "
text=x.format("phyton","javascript","html")
print(text)
import math
x=max(10,20,30)
print(x)
import random
x= random.randint(0,10)
print(x)
import datetime
now = datetime.datetime.now()
print(now)
