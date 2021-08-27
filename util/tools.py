# -*- coding: utf-8 -*-

import os
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
