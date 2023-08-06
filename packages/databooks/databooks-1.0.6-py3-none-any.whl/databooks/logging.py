"""Logging helper functions."""

import logging
import os

from rich.logging import RichHandler


def get_logger(name: str) -> logging.Logger:
    """Get logger with rich configuration."""
    level = os.getenv("LOG_LEVEL", logging.INFO)
    logging.basicConfig(
        level=level,
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(rich_tracebacks=True)],
    )
    return logging.getLogger(name)


def set_verbose(logger: logging.Logger) -> None:
    """Set logger to DEBUG level when user requests verbosity."""
    verbose_level = logging.DEBUG
    logger.setLevel(verbose_level)
    logger.debug(
        f"Verbose mode: setting log level to {logging.getLevelName(verbose_level)}"
    )
