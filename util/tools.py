# -*- coding: utf-8 -*-

import os
import json
from pathlib import Path
from util.config import Config


def get_config_value(section, key):
    cfg_dir = Path(__file__).parent.parent
    cfg = Config(cfg_dir, 'config.ini')
    return cfg.get_content(section).get(key)


def get_config_section(section):
    cfg_dir = Path(__file__).parent.parent
    cfg = Config(cfg_dir, 'config.ini')
    return cfg.get_content(section)

def get_json_file(file_path):
    if not os.path.exists(file_path):
        return None

    with open(file_path, 'r', encoding='utf-8') as f:
        json_data = json.loads(f.read())
        return json_data