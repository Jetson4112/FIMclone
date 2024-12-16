#/////IMPORT STATEMENTS/////#
import random
import time
print("this is addition pracitce script")
#time.sleep(2)
#print()
#print(random.randint(0,10)) #DEBUG --> generating random numbers 


def addScript ():
    one = random.randint(0,10)
    two = random.randint(0,10)
    ans = one + two
    if ans == int(input("What is " + str(one) + " + " + str(two) + " ?")):
        print("correct")
        passed = True
    else:
        print("wrong")
        passed = False
    return(passed)
#print(addScript())#DEBUG
