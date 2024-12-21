#/////IMPORT STATEMENTS/////#
import random
import time
print("this is addition pracitce script")
#time.sleep(2)
#print()
#print(random.randint(0,10)) #DEBUG --> generating random numbers 

def timer( start: int, endVal: int, step :int, timerMessage : str, endMessage : str) :
    for i in range(start, endVal, step):
        print(timerMessage, str(i), end = "\r")
        time.sleep(abs(step))
    print(" " * (len(timerMessage) + 5))
    print(endMessage, "\n")
timer(3, 0, -1, "Clock is ticking!!!", "Time is up!!!")

def addScript ():
    one = random.randint(0,10)
    two = random.randint(0,10)
    ans = one + two
    print(inAns + "<--- inAns")
    inAns = input("What is {one} + {two} + ?")
    """timer(3, 0, -1, "Clock is ticking!!!", "Time is up!!")
    if ans == int(inAns):
        print("correct")
        passed = True
    else:
        print("wrong")
        passed = False
    return(passed)"""
addScript()
#print(addScript())#DEBUG