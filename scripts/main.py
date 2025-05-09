global score, inVal
import time, webbrowser 
import var, screens       #screens is not accessed here; kept for redundancy
from var import passed, failed, devMode, timerLength, inVal, score
from screens import clear, intro, endScreen
from game import game

from logConfig import logging

if __name__ != "__main__":
    print("i dunno man")


log = logging.getLogger("mainLogger")

intro()

while True:
    if failed.is_set():
        log.debug(f"triggered flag (failed) {failed}")
        break    
    #menu selection settings
    #        V    
    match var.get("inVal"):
        case value if value in {"1" , "2" , "3"}: #game modes(as set in game function)
            log.debug(f"triggering game(); inVal = {var.get("inVal")}")
            game()
        #additional menu options beyond this point
        
        case "quit":
            log.debug("trigerred endscreen")
            endScreen()
            break
        
        case "reset":
            clear()
            print('resetting')
            log.info("resetting")
            time.sleep(1)
            intro()
            break

        case "secrets":
            clear()
            print("rickroll activated")
            log.warning("youve been rickrolled")
            webbrowser.open_new("https://shattereddisk.github.io/rickroll/rickroll.mp4")
            break

        case None:
            try:
                raise ValueError("Recieving default value; is the variable assigned?")
            except ValueError:
                log.exception("menu logic misconfigured in main; make sure to add options to main.py and game() in game.py")
                raise
        
        case __ :
            log.debug("triggered fallback for menu; no such options configured")
            clear()
            print(var.get("inVal"))
            print("\ninvalid input")
            time.sleep(2)
            intro()

log.info("ended execution")


