import logging
import os
import sys

log_formatter = logging.Formatter("%(asctime)s [%(levelname)-5.5s]  %(message)s")
logger = logging.getLogger()

# create a file handler which will have everything written out to it
file_handler = logging.FileHandler(os.path.join(".", "sentiment_analyst.log"))
file_handler.setFormatter(log_formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(file_handler)

# create a stream handler that will write just INFO messages or more important
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(log_formatter)
console_handler.setLevel(logging.INFO)

logger.addHandler(console_handler)
logger.setLevel(logging.DEBUG)
