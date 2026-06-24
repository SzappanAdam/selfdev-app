import logging
import os

LOG_FILE = "app.log"

logger = logging.getLogger("selfdev")

logger.setLevel(logging.INFO)

# ha már van handler, ne duplikáljuk
if not logger.handlers:

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)