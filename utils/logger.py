import sys
from loguru import logger

def configure_logging(verbose: bool):
    logger.remove()

    logger.add(
        "osi_simulation.log",
        level="DEBUG",
        rotation="500 KB",
        retention=5,
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}"
    )

    logger.add(
        sys.stdout,
        level="DEBUG" if verbose else "INFO",
        format="{time:HH:mm:ss} | {level} | {message}"
    )
