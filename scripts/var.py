import threading

#this file dictates the default values for the script at initialization
#it also serves as a exchange point for files to communicate

#make sure to use "var. <var_name>" format to dynamically access variables across files

#use "from var import <var_name>", and call <var_name> to use constant values

inVal = "-1"
debugMode = False #set to true to enable flow control print statements
passed = threading.Event()
failed = threading.Event()
timerEnd = threading.Event()
score = 0
timerLength = 5
userMode = -1