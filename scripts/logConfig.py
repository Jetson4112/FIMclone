import logging, sys
import logging.config

handlerList = ["consoleHandler", "fileHandler"]
txtLevel = "WARNING"
fileLevel = "INFO"
log_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "loggers": {
        "gameLogger": {
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
            "handlers": handlerList,
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
            "class":"logging.FileHandler",
            "formatter":"verboseFormatter",
            "level":fileLevel,
            "filename":"app.log",
            "mode":"w",
        }
    },
    
    "root": {
        "level": "NOTSET",
        "handlers": handlerList
    },
}

logging.config.dictConfig(log_config)
