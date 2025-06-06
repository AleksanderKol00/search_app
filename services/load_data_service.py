import logging
from typing import Optional

log = logging.getLogger(__name__)


def get_data_from_file(file_path: str) -> list[Optional[int]]:
    log.info(f"Loading data from file path: {file_path}")
    try:
        with open(file_path, 'r') as file:
            file_data = [int(line.strip()) for line in file]
    except FileNotFoundError:
        log.error(f"File {file_path} not found")
        raise
    except Exception as e:
        log.error(f"Failed to load data from file {file_path}: {e}")
        raise
    log.info(f"Successfully loaded data from file {file_path}")
    return file_data
