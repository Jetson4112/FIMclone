import time

import var

#this code is a mess
#id greatly appreciate cleaning it up a bit

from var import passed, failed, debugMode


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
                    raise TimeoutError("you ran out of time")
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
                raise TimeoutError("you ran out of time")
                
        except TimeoutError:
            if debugMode:
                print("timer passed")
                pass 
            else:
                pass
            return   
        
if __name__ == "__main__":
    timer(0, 3)