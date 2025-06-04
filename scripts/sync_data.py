#!/usr/bin/env python3
# Helper script to sync or validate data files

import json
import os

def validate_json_files(data_dir):
    for fname in os.listdir(data_dir):
        if fname.endswith('.json'):
            try:
                with open(os.path.join(data_dir, fname), 'r', encoding='utf-8') as f:
                    json.load(f)
                print(f"{fname}: OK")
            except Exception as e:
                print(f"{fname}: ERROR - {e}")

if __name__ == "__main__":
    validate_json_files(os.path.join(os.path.dirname(__file__), '../data'))
