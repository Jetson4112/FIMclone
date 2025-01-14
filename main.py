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

<<<<<<< Updated upstream
def timer_countDown_(endVal: int, start: int = 0 , step :int = -1, timerMessage : str = "timer running...", endMessage : str = "timer ended") :
=======
def timer(endVal: int, 
                     start: int = 0 ,
                     step :int = -1, 
                     timerMessage : str = "Timer running...",
                     endMessage : str = "Timer ended. Press ENTER to continue:") :
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
        return
=======
        return   
    
def intro():
    clear()
    print("""Welcome to Arithmetics Range. this app is still a WIP. Report bugs on the GitHub page.
    Enter the Numbers to select yor input;
        1.Addition
        2.Subtraction
        3.Multiplication""")
    time.sleep(1)
>>>>>>> Stashed changes

intro()
while True:
    inVal = input("\nEnter your response-->")
    if (input(f"you entered \"{inVal}\"; type \'y\' once you're ready, or press[ENTER] to reset:").lower()) == "y":
        match inVal:
            case "1":
                add()
                break
            case "2":
                #sub()
                print("subtaction range is coming soon")
                break
            case "3:":
                print("multiplication range is coming soon")
                
            case __:
                print("invalid input")
                continue
    else:
        intro()
        pass

threadTimer = threading.Thread(target = timer, args=(0, timerLength , -1,"Clock is ticking!!!", "Time is up!!"))
threadScript = threading.Thread(target=add())
threadScript.start()
<<<<<<< Updated upstream
#threadInDebug.start()
threadTimer.start()
=======
threadTimer.start()
threadScript.join()         #join threads to ensure everything has executed successfully
threadTimer.join()          #<same here>
clear()
print("\nthanks for playing!!")
>>>>>>> Stashed changes
