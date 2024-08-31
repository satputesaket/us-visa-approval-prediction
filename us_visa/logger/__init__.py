import logging
import os

from datetime import datetime





LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_dir = "logs"

logs_path = os.path.join("/Users/saket/Documents/MLOPS/usa-visa-approval-prediction/", log_dir, LOG_FILE)

print(logs_path)
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(filename=logs_path, 
                    level=logging.INFO, 
                    format='%(asctime)s %(levelname)s %(message)s', 
                    datefmt='%Y-%m-%d %H:%M:%S')