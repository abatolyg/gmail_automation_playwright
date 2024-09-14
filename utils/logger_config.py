import logging
import os
from dotenv import load_dotenv

load_dotenv()

def setup_logger(name):
    """Set up a logger with a file handler and a console handler."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Create handlers
    log_file_path = os.getenv("LOG_FILE_PATH", "app.log")
    file_handler = logging.FileHandler(log_file_path)
    console_handler = logging.StreamHandler()

    # Create formatters and add them to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

# Set up the root logger
logger = setup_logger(__name__)