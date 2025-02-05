import threading

inVal = "-1"
debugMode = False #set to true to enable flow control print statements
passed = threading.Event()
failed = threading.Event()
timerEnd = threading.Event()
score = 0
timerLength = 5
userMode = -1