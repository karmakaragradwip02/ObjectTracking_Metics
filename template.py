import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "CHESS_PIECE_DETECTION"

list_of_files = [
    ".github/workflows/.gitkeep",
    "metrics/mota.py",
    "metrics/hota.py",
    "metrics/assa.py",
    "metrics/deta.py",
    "metrics/idsw.py",
    "metrics/idt_pn.py",
    "metrics/idf_pn.py",
    "metrics/idf1.py",
    "config/config.yaml",
    "requirements.txt",
    "setup.py",
    "main.py",
    "research/trials.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating Directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    
    else:
        logging.info(f"{filename} is already exists")