import logging
import os
from datetime import datetime

# Create logs directory if it doesn't exist
logs_dir = os.path.join(os.getcwd(), 'logs')
os.makedirs(logs_dir, exist_ok=True)

# Generate log file name
log_file = datetime.now().strftime('%m_%d_%Y_%H_%M_%S') + '.log'
log_file_path = os.path.join(logs_dir, log_file)

# Set up logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(filename=log_file_path),
        logging.StreamHandler()
    ]
)

# Continue with your code...
if __name__ == '__main__':
    logging.info("Logging has started!")
