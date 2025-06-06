from typing import Optional


def get_data_from_file(file_path: str) -> list[Optional[int]]:
    try:
        with open(file_path, 'r') as file:
            file_data = [int(line.strip()) for line in file]
    except FileNotFoundError:
        print('File not found')
        raise
    except Exception as e:
        print(e)
        raise
    return file_data
