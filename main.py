global score, inVal
import time, webbrowser 
import var, screens 
#screens is not accessed here; kept for redundancy
from var import passed, failed, debugMode, timerLength, inVal, score
from screens import clear, intro, endScreen
from game import game

if __name__ != "__main__":
    print("i dunno man")

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



