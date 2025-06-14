import random, threading

import var

from screens import clear, endScreen
from timer import timer # type: ignore
from logConfig import logging

log = logging.getLogger("gameLogger")



def numGen():
    while True:    
        if var.get("passed").is_set() or var.get("failed").is_set():
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
            var.get("passed").set()
            var.get("failed").clear()
            clear()
        elif inAns == "" :
            pass
        else:
            print("...wrong")
            var.get("passed").clear()
            var.get("failed").set()
        return(var.get("passed").is_set())
    
def game():
    var.get("passed").clear()
    var.get("failed").clear()
    
    threadTimer = threading.Thread(target = timer, args=(0, var.get("timerLength") , -1),daemon=True)
    threadAdd = threading.Thread(target=numGen, daemon=True) 

    threadAdd.start()
    threadTimer.start()
    while True:

        if var.get("failed").is_set():
            endScreen()
            break
        elif var.get("passed").is_set():
            global score
            var.set("score", var.get("score") + 1) #WIP dont look ;)
            break
        threadAdd.join()            #join threads to ensure everything has executed successfully
        threadTimer.join()

if __name__ == "__main__":
    game()
