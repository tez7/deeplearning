import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]" # Define the logging format

log_dir = "logs" # Directory to store log files
log_filepath = os.path.join(log_dir,"running_logs.log") # Full path for the log file
os.makedirs(log_dir, exist_ok=True) # Create the log directory if it doesn't exist


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("cnnClassifierLogger")