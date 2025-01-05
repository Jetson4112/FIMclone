import time
import random
import threading
debugMode = False #set to true to enable flow control print statements
passed = threading.Event()
failed = threading.Event()
timerEnd = threading.Event()
timerLength = 5

def addScript ():
    if debugMode:
        one, two = 1, 2 
        pass 
    else:
        one = random.randint(0,10)
        two = random.randint(0,10)
        pass

    ans = one + two
    inAns = input("What is " + str(one) + " + " + str(two) + " + ?")
    if debugMode:
        print(inAns)
        pass 
    else:
        pass
    if ans == int(inAns):
        print("correct")
        passed.set()
        failed.clear()
    else:
        print("wrong")
        passed.clear()
        failed.set()
    return(passed)

def timer_countDown_(endVal: int, start: int = 0 , step :int = -1, timerMessage : str = "timer running...", endMessage : str = "timer ended") :
    print("\n")
    print("\n")
    try:
        for i in range(start, endVal, step):
            if debugMode:
                print("\n=======================================================\n")
                pass 
            else:
                pass
            if (passed.is_set()):
                ##uncomment for debug
                if debugMode:
                    print("\ntriggered exit in timer\n")
                    pass 
                else:
                    pass
                raise SystemExit
                #exit here
            elif (failed.is_set()):
                if debugMode:
                    print("\ntriggered exit in timer\n")
                    pass 
                else:
                    pass
                raise SystemExit
            else:
                if debugMode:
                    print("\nchecking passed........................")
                    pass 
                else:
                    pass
                pass    
            if debugMode:
                print("passed " + str(passed))
                pass 
            else:
                pass
            print(timerMessage, str(i), end = "\r")
            time.sleep(abs(step))
        if (not passed.is_set()):
            print(" " * (len(timerMessage) + 5))
            print(endMessage, "\n")
            return
    except SystemExit:
        if debugMode:
            print("timer ended")
            pass 
        else:
            pass
        return



def inDebug(): 
    i = input("debug mode")
    if i != "":
        exit()

threadTimer = threading.Thread(target = timer_countDown_, args=(0, timerLength)) #"Clock is ticking!!!", "Time is up!!"
threadScript = threading.Thread(target=addScript)
threadInDebug = threading.Thread(target = inDebug)
threadScript.start()
#threadInDebug.start()
threadTimer.start()
