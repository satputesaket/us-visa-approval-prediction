import logging
import os
from from_root import from_root;
from datetime import datetime





LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_dir = "logs"

logs_path = os.path.join(from_root(), log_dir, LOG_FILE)

print(logs_path)
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(filename=logs_path, 
                    level=logging.INFO, 
                    format='%(asctime)s %(levelname)s %(message)s', 
                    datefmt='%Y-%m-%d %H:%M:%S')