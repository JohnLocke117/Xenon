"""
Defines a custom color-coded logging format using colorlog
"""

import logging
from logging.config import dictConfig


class UvicornAccessLogFilter(logging.Filter):
    """
    Set Uvicorn Access Log level based on Error Code
    """

    def filter(self, record: logging.LogRecord) -> bool:
        args = record.args

        if not isinstance(args, tuple) or len(args) < 5:
            return True
        
        status_code = args[4]
        if not isinstance(status_code, int):
            return True

        # Set the Log Level
        if status_code >= 500:
            record.levelno = logging.ERROR
            record.levelname = "ERROR"
        elif status_code >= 400:
            record.levelno = logging.WARNING
            record.levelname = "WARNING"

        return True


def setup_logging(level: str = "INFO") -> None:
    """
    Define the Custom Logging Format

    Args:
        level: The log-level for the logs (set to INFO)
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
            "filters": {
                "uvicorn_access_level": {
                    "()": UvicornAccessLogFilter,
                },
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "formatter": "colored",
                },
                "uvicorn_access_console": {
                    "class": "logging.StreamHandler",
                    "formatter": "colored",
                    "filters": ["uvicorn_access_level"],
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
                    "handlers": ["uvicorn_access_console"],
                    "level": level,
                    "propagate": False,
                },
            },
        }
    )
