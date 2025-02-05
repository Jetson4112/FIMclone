global score, inVal
import time
import random
import threading
import os
import webbrowser
import var, screens 
#screens is not accessed here; kept for redundancy
from var import passed, failed, debugMode, timerLength, inVal, score
from screens import clear, intro


  

def numGen():
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
        print("reached match case")
        match var.inVal:
            case "1":
                ans = one + two #addition
                displayMessage = "What is " + str(one) + " + " + str(two) + " ?"
                pass
            case "2":
                ans = one - two #subtraction
                displayMessage = "What is " + str(one) + " - " + str(two) + " ?"
                pass
            case "3":
                ans = one * two #multiplication
                displayMessage = "What is " + str(one) + " × " + str(two) + " ?"
                pass
            case __:
                raise ValueError("game mode not found(is it in the match case at game function?)")
            

        #inAns = input(displayMessage) #deprecated
        print(displayMessage, "\n")
        inAns = input("your answer:     \n")
        if debugMode:
            print(inAns)
            pass 
        else:
            pass

        if str(ans) == inAns:
            print("correct!")
            passed.set()
            failed.clear()
            clear()
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
                if (passed.is_set() or failed.is_set()):
                    ##uncomment for debug
                    if debugMode:
                        print("\ntriggered exit in timer\n")
                        pass 
                    else:
                        pass
                    raise SystemExit
                    #exit here
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
  

def endScreen():
    time.sleep(1)
    clear()
    print(f" your score was {score}")
    print("\nthanks for playing!!")
    time.sleep(1)

def game():
    passed.clear()
    failed.clear()
    
    threadTimer = threading.Thread(target = timer, args=(0, timerLength , -1,"Clock is ticking!!!"),daemon=True)
    threadAdd = threading.Thread(target=numGen, daemon=True) 

    threadAdd.start()
    threadTimer.start()
    while True:

        if failed.is_set():
            endScreen()
            break
        elif passed.is_set():
            global score
            score += 1 #WIP dont look ;)
            break
        threadAdd.join()            #join threads to ensure everything has executed successfully
        threadTimer.join()          #<same here> 
                
intro()

while True:
    if failed.is_set():
        break    
    #menu selection settings
    #        V    
    match var.inVal:
        case v if v in {"1" , "2" , "3"}: #game modes(as set in game function)
            game()
        #additional menu options beyound this point
        case "quit":
            endScreen()
            break
        
        case ("reset", ""):
            clear()
            intro()
            break
        case "secrets":
            clear()
            print("rickroll activated")
            webbrowser.open_new("https://shattereddisk.github.io/rickroll/rickroll.mp4")
            break
        
        case "-1":
            raise ValueError("Recieving default value; is the variable assigned?")
        
        case __ :
            clear()
            print("invalid input")
            time.sleep(2)
            intro()



