import logging, sys, inspect
import logging.config

handlerList = ["consoleHandler", "fileHandler"]
txtLevel = "CRITICAL"
fileLevel = "INFO"
log_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "loggers": {
        "gameLogicLogger": {
            "handlers": handlerList,
            "level": "NOTSET",
            "propagate": False,
        },
        "mainLogger": {
            "handlers": handlerList,
            "level": "NOTSET",
            "propagate": False,
        },
        "screensLogger": {
            "handlers": handlerList,
            "level": "NOTSET",
            "propagate": False,
        },
        "timerLogger": {
            "handlers": handlerList,
            "level": "NOTSET",
            "propagate": False,
        },
        "varLogger": {
            "handlers": ["varFileHandler",],
            "level": "NOTSET",
            "propagate": False,
        },
    },
    "formatters": {
        "verboseFormatter": {
            "format": "%(asctime)s.%(msecs)03d - %(name)s - %(levelname)s - %(message)s",
            "datefmt": "%H:%M:%S",
        },
       
        "cleanFormatter": {
            "format": "%(name)s - %(levelname)s - %(message)s",
            "datefmt": "%H:%M:%S",
        },
    },
"handlers": {
    "consoleHandler": {
        "class": "logging.StreamHandler",
        "formatter": "cleanFormatter",
        "level": txtLevel,
        "stream": "ext://sys.stdout",
    },
    "fileHandler": {
        "class": "logging.FileHandler",
        "formatter": "verboseFormatter",
        "level": "INFO",
        "filename": "app.log",
        "mode": "w",
    },
    "varFileHandler": {
        "class": "logging.FileHandler",
        "formatter": "verboseFormatter",
        "level": "NOTSET",
        "filename": "var.log",
        "mode": "w",
    }
},

    
    "root": {
        "level": "NOTSET",
        "handlers": handlerList
    }

}
logging.config.dictConfig(log_config)

def lineLocator():
    frame = inspect.stack()[1]  # Get the calling function's stack frame
    caller = f"{frame.filename}:{frame.lineno}"  # File and line number of the caller
    return caller


if __name__ == "__main__":
    print("logConfig is main")