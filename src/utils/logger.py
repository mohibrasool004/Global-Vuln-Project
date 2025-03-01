"""
logger.py
---------
Sets up the project logging configuration.
"""

import logging
import os
import yaml

def get_logger(name):
    # Load logging configuration from config.yaml if available.
    try:
        config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '..', 'config', 'config.yaml')
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
            log_level = getattr(logging, config.get("logging", {}).get("level", "INFO").upper())
    except Exception:
        log_level = logging.INFO

    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(log_level)
        ch = logging.StreamHandler()
        ch.setLevel(log_level)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)
    return logger
