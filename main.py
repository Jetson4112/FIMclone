import time
import random
import threading
import os
debugMode = False #set to true to enable flow control print statements
passed = threading.Event()
failed = threading.Event()
timerEnd = threading.Event()
timerLength = 5
userMode = -1

def clear():
    
        if os.name == 'nt':
            _ = os.system('cls')# For Windows
        else:
            _ = os.system('clear')# For macOS and Linux

  

def add():
    if debugMode:
        one, two = 1, 2 
        pass 
    else:
        one = random.randint(0,10)
        two = random.randint(0,10)
        pass

    ans = one + two
    inAns = input("What is " + str(one) + " + " + str(two) + " ?")
    if debugMode:
        print(inAns)
        pass 
    else:
        pass
    if ans == int(inAns):
        print("correct!")
        passed.set()
        failed.clear()
    else:
        print("...wrong")
        passed.clear()
        failed.set()
    return(passed)

def timer(endVal: int, 
                     start: int = 0 ,
                     step :int = -1, 
                     timerMessage : str = "Timer running...",
                     endMessage : str = "Timer ended. Press ENTER to continue:") :
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
            #print(timerMessage, str(i), end = "\r") #deprecated
            print(f"{timerMessage:>100} [{str(i)}]", end="\r") #better formatted

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
threadTimer = threading.Thread(target = timer, args=(0, timerLength , -1,"Clock is ticking!!!", "Time is up!!"))
threadScript = threading.Thread(target=add)    
def intro():
    clear()
    print("""Welcome to Arithmetics Range. this app is still a WIP. Report bugs on the GitHub page.
    Enter the Numbers to select yor input;
        1.Addition
        2.Subtraction
        3.Multiplication""")
    time.sleep(1)

intro()

while True:
    inVal = input("\nEnter your response-->")
    if (input(f"you entered \"{inVal}\"; type \'y\' once you're ready, or press[ENTER] to reset:").lower()) == "y":
        match inVal:
            case "1":
                threadScript.start()
                threadTimer.start()
                threadScript.join()         #join threads to ensure everything has executed successfully
                threadTimer.join()          #<same here>
                break
            case "2":
                #sub()
                print("subtaction range is coming soon")
                continue
            case "3:":
                print("multiplication range is coming soon")
                continue
            case __:
                print("invalid input")
                continue
    else:
        intro()
        pass
time.sleep(2)
clear()
print("\nthanks for playing!!")
