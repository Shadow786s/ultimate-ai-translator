from loguru import logger
import sys

logger.remove()

logger.add(
    sys.stdout,
    level="INFO",
    enqueue=True,
    backtrace=True,
    diagnose=False
)

logger.add(
    "logs/server.log",
    rotation="10 MB",
    retention="30 days",
    level="INFO"
)
