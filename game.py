import random, threading

import var

from var import passed, failed, debugMode, timerLength, score
from screens import clear, endScreen
from timer import timer


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
        
        if debugMode:
            print("reached match case")
        else:
            pass

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
            var.score += 1 #WIP dont look ;)
            break
        threadAdd.join()            #join threads to ensure everything has executed successfully
        threadTimer.join()

if __name__ == "__main__":
    game()
