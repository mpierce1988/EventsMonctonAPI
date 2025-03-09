import json
import hashlib
from datetime import datetime

def calculate_row_hash(row: dict) -> str:
    def datetime_handler(obj):
        if isinstance(obj, datetime):
            return obj.isoformat()

        raise TypeError(f'Object of type {type(obj)} is not JSON Serializable')

    # Sort keys and enforce UTF8 to ensure consistency
    # json.dumps takes a Python object and serializes it
    # Enforce UTF-8 encoding, in the off-chance the default encoding changes (i.e. new Python version)
    row_str = json.dumps(row, sort_keys=True, default=datetime_handler).encode("utf-8")
    # Hash using SHA1. Convert binary representation into hexadecimal
    return hashlib.sha1(row_str).hexdigest()