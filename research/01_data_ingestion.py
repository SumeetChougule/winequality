import os

os.chdir("../")


from dataclasses import dataclass
from pathlib import Path
from src.wineQ.constants import *
from src.wineQ.utils.common import read_yaml, create_directories


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path
