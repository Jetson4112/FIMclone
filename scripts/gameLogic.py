import random, threading

import var

from var import passed, failed, devMode, timerLength, score
from screens import clear, endScreen
from timer import timer # type: ignore
from logConfig import logging

log = logging.getLogger("gameLogger")



def numGen():
    while True:    
        if passed.is_set() or failed.is_set():
            break

        if var.get("devMode"):
            numOne, numTwo = 1, 2 
            pass 
        else:
            numOne = random.randint(0,10)
            numTwo = random.randint(0,10)
            pass
        
        log.info("reached match-case")
        global question

        match var.get("inVal"):
            case "1":
                ans = numOne + numTwo #addition
                question = "What is " + str(numOne) + " + " + str(numTwo) + " ?"
                pass
            case "2":
                ans = numOne - numTwo #subtraction
                question = "What is " + str(numOne) + " - " + str(numTwo) + " ?"
                pass
            case "3":
                ans = numOne * numTwo #multiplication
                question = "What is " + str(numOne) + " × " + str(numTwo) + " ?"
                pass
            case __:
                try:
                    raise ValueError("game mode not found")
                except:
                    log.critical("value not found in match case(is it in the match case at game function in game.py?)")
            

        print(question, "\n")
        inAns = input("your answer:     \n")
        log.debug(f"inAns {inAns}")

        if str(ans) == inAns:
            print("correct!")
            passed.set()
            failed.clear()
            clear()
        elif inAns == "" :
            pass
        else:
            print("...wrong")
            passed.clear()
            failed.set()
        return(passed.is_set())
    
def game():
    passed.clear()
    failed.clear()
    
    threadTimer = threading.Thread(target = timer, args=(0, timerLength , -1),daemon=True)
    threadAdd = threading.Thread(target=numGen, daemon=True) 

    threadAdd.start()
    threadTimer.start()
    while True:

        if failed.is_set():
            endScreen()
            break
        elif passed.is_set():
            global score
            var.set("score", var.get("score") + 1) #WIP dont look ;)
            break
        threadAdd.join()            #join threads to ensure everything has executed successfully
        threadTimer.join()

if __name__ == "__main__":
    game()
