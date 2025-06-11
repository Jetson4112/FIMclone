import time

import var, screens

#this code is a mess
#id greatly appreciate cleaning it up a bit



from logConfig import logging

log = logging.getLogger("timerLogger")

def timer(
endVal: int = 0, 
start: int = 3 ,
step :int = -1,
clockSpeed : float = 1,  
timerMessage : str = "Timer running...",
endMessage : str = "Timer ended. Press ENTER to continue:") :


    while True:
        if var.get("passed").is_set() or var.get("failed").is_set():
            break
        print("\n")
        print("\n")
        try:
            for secs in range(start, endVal, clockSpeed*step):
                var.set("secs", secs)
                log.info("\n=======================================================\n")
                
                if (var.get("passed").is_set() or var.get("failed").is_set()):
                    log.debug("\ntriggered exit in timer\n")
                    raise TimeoutError("you passed or failed")
                    #exit here
                else:
                    log.debug("\nchecking passed........................")
                    pass    
                
                log.debug(f"Timer tick: {var.get("secs")} | passed: {var.get("passed").is_set()} | failed: {var.get("failed").is_set()}")
                
                #print(f"{timerMessage:>100} [{str(var.get("secs"))}]", end="\r") #better formatted
                #line 42 not used as everything is replaced to function
                screens.questionScreen()
                
                time.sleep(abs(step))


            if ((not var.get("passed").is_set()) and (not var.get("failed").is_set())):
                print(" " * (len(timerMessage) + 5))
                
                log.info("triggering endmesage")
                print(endMessage, "\n")
                raise TimeoutError("you ran out of time")
                
        except TimeoutError:
            if var.get("passed").is_set():
                log.info("passed is set")
                log.debug(f"""passed {var.get("passed")}\n failed {var.get("failed")}""")
            elif var.get("failed").is_set():
                log.info("failed is set")
                log.debug(f"""passed {var.get("passed")}\n failed {var.get("failed")}""")
            else:
                log.error("timeout trigerred")
            return   
        
if __name__ == "__main__":
    timer(0, 3, step=1, clockSpeed=2)