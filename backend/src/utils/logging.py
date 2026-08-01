"""
This file defines our global custom logging format.
Utilises colorlog for color-coded logs and
a custom JSON design 
"""

from logging.config import dictConfig


def setup_logging(level: str = "INFO") -> None:
    """
    Define the Custom Logging Format

    Args:
        level: The log-level for the logs (set to INFO)
    
    Returns:
        None
    """

    dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "colored": {
                    "()": "colorlog.ColoredFormatter",
                    "format": (
                        "%(asctime)s | "
                        "%(log_color)s%(levelname)-8s%(reset)s | "
                        "PID:%(process)-6d | "
                        "%(name)-20s | "
                        "%(filename)-12s:%(lineno)-4d | "
                        "%(message_log_color)s%(message)s%(reset)s"
                    ),
                    "datefmt": "%d-%m-%Y %H:%M:%S",
                    "log_colors": {
                        "DEBUG": "cyan",
                        "INFO": "green",
                        "WARNING": "yellow",
                        "ERROR": "red",
                        "CRITICAL": "bold_red",
                    },
                    "secondary_log_colors": {
                        "message": {
                            "DEBUG": "cyan",
                            "INFO": "green",
                            "WARNING": "yellow",
                            "ERROR": "red",
                            "CRITICAL": "bold_red",
                        }
                    },
                }
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "formatter": "colored",
                },
            },
            "root": {
                "handlers": ["console"],
                "level": level,
            },
            "loggers": {
                "uvicorn": {
                    "handlers": ["console"],
                    "level": level,
                    "propagate": False,
                },
                "uvicorn.error": {
                    "handlers": ["console"],
                    "level": level,
                    "propagate": False,
                },
                "uvicorn.access": {
                    "handlers": ["console"],
                    "level": level,
                    "propagate": False,
                },
            },
        }
    )
