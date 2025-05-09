import threading, inspect
from logConfig import logging
log = logging.getLogger("varLogger")

#this file dictates the default values for the script at initialization
#it also serves as a exchange point for files to communicate

#make sure to use "var. <var_name>" format to dynamically access variables across files

#use "from var import <var_name>", and call <var_name> to use constant values

# it is recomended to use get and set functions, otherwise use older notation for quiet r/w
defaultValues = {
"inVal" : None,
"devMode" : False, #set to true to stop randomisation
"passed" : threading.Event(),
"failed" : threading.Event(),
"timerEnd" : threading.Event(),
"score" : 0,
"timerLength" : 5,
"userMode" : -1 } 

def get(name : str):
    frame = inspect.stack()[1]  # Get the calling function's stack frame
    caller = f"{frame.filename}:{frame.lineno}"  # File and line number of the caller
    value = defaultValues[name]
    log.info(f"[get()] {name} accessed; value \'{value}\' returned(called from {caller})")
    return value

def set(name : str, value):
    frame = inspect.stack()[1]  # Get the calling function's stack frame
    caller = f"{frame.filename}:{frame.lineno}"  # File and line number of the caller
    oldValue = defaultValues[name]
    defaultValues[name] = value
    log.info(f"[set()] {name} modified; {name} : {oldValue} --> {value} (from {caller})")

#kept for redundancy

inVal = None
devMode = False #set to true to enable flow control print statements
passed = threading.Event()
failed = threading.Event()
timerEnd = threading.Event()
score = 0
timerLength = 5
userMode = -1