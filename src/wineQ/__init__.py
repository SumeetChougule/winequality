import logging
from pathlib import Path

# Set up logging
log_file_path = Path("logs/wineQ_project.log")
log_file_path.parent.mkdir(
    parents=True, exist_ok=True
)  # Create the log directory if it doesn't exist

logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
