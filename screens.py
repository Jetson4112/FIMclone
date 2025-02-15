import os, time

import var

from var import score


def clear():
    
        if os.name == 'nt':
            _ = os.system('cls')# For Windows
        else:
            _ = os.system('clear')# For macOS and Linux

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
    
    var.inVal = input("\nEnter your response-->")


def endScreen():
    time.sleep(1)
    clear()
    print(f" your score was {var.score}")
    print("\nthanks for playing!!")
    time.sleep(1)

if __name__ == "__main__":
    intro()
