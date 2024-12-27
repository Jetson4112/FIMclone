import time
import random
import threading
debugMode = False
passed = threading.Event()

def addScript ():
    one = random.randint(0,10)
    two = random.randint(0,10)
    #one, two = 1, 2 #uncomment for debug
    ans = one + two
    inAns = input("What is " + str(one) + " + " + str(two) + " + ?")
    #print(inAns)#uncomment for debug
    if ans == int(inAns):
        print("correct")
        passed.set()
    else:
        print("wrong")
        passed.clear()
    return(passed)

def timer( start: int, endVal: int, step :int, timerMessage : str, endMessage : str) :
    print("\n")
    print("\n")
    try:
        for i in range(start, endVal, step):
            #print("\n=======================================================\n")#uncomment for debug
            if (passed.is_set()):
                #print("\ntriggered exit in timer\n")#uncomment for debug
                raise SystemExit
                #exit here
            else:
                #print("\nchecking passed........................")
                pass    
            #print("passed " + str(passed))         #uncomment for debug
            print(timerMessage, str(i), end = "\r")
            time.sleep(abs(step))
        if (not passed.is_set()):
            print(" " * (len(timerMessage) + 5))
            print(endMessage, "\n")
    except SystemExit:
        #print("timer ended")       #uncomment for debug
        return
def inDebug(): 
    i = input("debug mode")
    if i != "":
        exit()

threadTimer = threading.Thread(target = timer, args=(5, 0, -1, "Clock is ticking!!!", "Time is up!!"))
threadScript = threading.Thread(target=addScript)
threadInDebug = threading.Thread(target = inDebug)
threadScript.start()
#threadInDebug.start()
threadTimer.start()
