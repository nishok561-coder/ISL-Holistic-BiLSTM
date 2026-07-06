"""
=========================================================
Project : ISL Non-Manual Feature Recognition
File    : logger.py
Purpose : Configure project-wide logging
=========================================================
"""

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger("ISL_Project")