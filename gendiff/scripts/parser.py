import json
import os
from typing import Any, Dict

import yaml


def parse_file(file_path: str) -> Dict[str, Any]:
    _, ext = os.path.splitext(file_path.lower())

    with open(file_path, 'r', encoding='utf-8') as file_object:
        if ext == '.json':
            return json.load(file_object)
        if ext in {'.yml', '.yaml'}:
            data = yaml.safe_load(file_object)
            return data or {}

    raise ValueError(f'Unsupported file extension: {ext}')
