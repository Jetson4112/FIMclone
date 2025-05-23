import os, time
from logConfig import logging

import var

#from var import score #deemed unneded
log = logging.getLogger("screensLogger")
def clear():
    log.debug("triggered clear()")
    if os.name == 'nt':
        _ = os.system('cls')# For Windows
    else:
        _ = os.system('clear')# For macOS and Linux
    log.info("cleared screen")

def intro():
    clear()
    print(
    """Welcome to Arithmetics Range. this app is still a WIP. Report bugs on the GitHub page.
    
    Enter the Numbers to select your input;
    The game will start as soon as you press enter with your choice
        1. Addition
        2. Subtraction
        3. Multiplication
    reset. reset the main menu
     quit. quit this program""")
    time.sleep(1)
    log.debug("printed menu")
    var.set("inVal", input("\nEnter your response-->"))
    log.info(f"inVal = {var.get("inVal")}")


def endScreen():
    time.sleep(1)
    clear()
    print(f"your score was {var.get("score")}")
    print("\nthanks for playing!!")
    time.sleep(1)
    log.info("ended execution")

def questionScreen():
    from gameLogic import question#, end="\r"  from print statement
    clear()
    print(f"""
        {question}


       {"Clock is ticking!!!":>100} [{str(var.get("secs"))}]


       Your answer:
       \n""")
    
    

if __name__ == "__main__":
    intro()
