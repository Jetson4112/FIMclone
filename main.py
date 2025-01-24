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
global score, inVal
score = 0
def clear():
    
        if os.name == 'nt':
            _ = os.system('cls')# For Windows
        else:
            _ = os.system('clear')# For macOS and Linux

  

def add():
    while True:    
        if passed.is_set() or failed.is_set():
            break
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

        if str(ans) == inAns:
            print("correct!")
            passed.set()
            failed.clear()
        elif inAns == "":
            pass
        else:
            print("...wrong")
            passed.clear()
            failed.set()
        return(passed.is_set())


def timer(endVal: int, 
                     start: int = 0 ,
                     step :int = -1, 
                     timerMessage : str = "Timer running...",
                     endMessage : str = "Timer ended. Press ENTER to continue:") :

    while True:
        if passed.is_set() or failed.is_set():
            break
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
            if ((not passed.is_set()) and (not failed.is_set())):
                print(" " * (len(timerMessage) + 5))
                if debugMode:
                    print("triggering endMessage")
                    pass 
                else:
                    pass
                print(endMessage, "\n")
                raise SystemExit
                
        except SystemExit:
            if debugMode:
                print("timer passed")
                pass 
            else:
                pass
            return   
#threadTimer = threading.Thread(target = timer, args=(0, timerLength , -1,"Clock is ticking!!!", "Time is up!!"),daemon=True)
#threadAdd = threading.Thread(target=add, daemon=True) #unneded
  
def intro():
    clear()
    print(
    """Welcome to Arithmetics Range. this app is still a WIP. Report bugs on the GitHub page.
    
    Enter the Numbers to select your input;
    the game will start as soon as you press enter with your choice
        1. Addition
        2. Subtraction
        3. Multiplication
    reset. reset the main menu
     quit. quit this program""")
    time.sleep(1)
    global inVal
    inVal = input("\nEnter your response-->")

def endScreen():
    time.sleep(1)
    clear()
    print("\nthanks for playing!!")
    time.sleep(1)

def game_add():
    passed.clear()
    failed.clear()
    
    threadTimer = threading.Thread(target = timer, args=(0, timerLength , -1,"Clock is ticking!!!"),daemon=True)
    threadAdd = threading.Thread(target=add, daemon=True) 

    threadAdd.start()
    threadTimer.start()
    while True:

        if failed.is_set():
            endScreen()
            break
        elif passed.is_set():
            #score += 1 WIP dont look ;)
            break
        threadAdd.join()            #join threads to ensure everything has executed successfully
        threadTimer.join()          #<same here> 
                
intro()

while True:
    if failed.is_set():
        break
    #inVal = input("\nEnter your response-->")
    #if (input(f"you entered \"{inVal}\"; type \'y\' once you're ready, or press[ENTER] to reset:").lower()) == "y": #a relic of the past, unnecessary for now
    
    #menu selection settings
    #        V    
    match inVal:
        case "1":
            game_add()
        case "2":
            #sub()
            print("subtaction range is coming soon")
            continue
        case "3":
            print("multiplication range is coming soon")
            continue
        case "quit":
            endScreen()
            break     #exit the program
        case "reset":
            intro()
            pass
        case __:
            clear()
            print("invalid input")
            time.sleep(2)
            inVal = "reset"



