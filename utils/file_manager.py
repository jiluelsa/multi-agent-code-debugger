import os
from pathlib import Path


def load_code(file_path: str = "workspace/my_code.py") -> str:
    """
    Load code from the file that pytest also imports.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Code file not found: {file_path}")
    except Exception as e:
        raise Exception(f"Error loading code file: {e}")


def save_code(code: str, file_path: str = "workspace/my_code.py") -> None:
    """
    Save refactored code back into the exact file the tests run against.
    """
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(code)

    except Exception as e:
        raise Exception(f"Error saving code file: {e}")
