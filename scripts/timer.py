import time

import var

#this code is a mess
#id greatly appreciate cleaning it up a bit

from var import passed, failed

from logConfig import logging

log = logging.getLogger("timerLogger")

def timer(
endVal: int = 0, 
start: int = 3 ,
step :int = -1, 
timerMessage : str = "Timer running...",
endMessage : str = "Timer ended. Press ENTER to continue:") :


    while True:
        if passed.is_set() or failed.is_set():
            break
        print("\n")
        print("\n")
        try:
            for secs in range(start, endVal, step):
                var.set("secs", secs)
                log.info("\n=======================================================\n")
                
                if (passed.is_set() or failed.is_set()):
                    log.debug("\ntriggered exit in timer\n")
                    raise TimeoutError("you passed or failed")
                    #exit here
                else:
                    log.debug("\nchecking passed........................")
                    pass    
                
                log.debug(f"Timer tick: {i} | passed: {passed.is_set()} | failed: {failed.is_set()}")
                
                print(f"{timerMessage:>100} [{str(i)}]", end="\r") #better formatted
                
                time.sleep(abs(step))


            if ((not passed.is_set()) and (not failed.is_set())):
                print(" " * (len(timerMessage) + 5))
                
                log.info("triggering endmesage")
                print(endMessage, "\n")
                raise TimeoutError("you ran out of time")
                
        except TimeoutError:
            if passed.is_set():
                log.info("passed is set")
                log.debug(f"""passed {passed}\n failed {failed}""")
            elif failed.is_set():
                log.info("failed is set")
                log.debug(f"""passed {passed}\n failed {failed}""")
            else:
                log.error("timeout trigerred")
            return   
        
if __name__ == "__main__":
    timer(0, 3)