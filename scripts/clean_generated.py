"""
============================================================
Module Name : clean_generated.py
Author      : javaboy-vk
Date        : 2026-05-22
Version     : 1.0
Description : Removes generated MAGPAI build and documentation output.
============================================================
"""

from pathlib import Path
import shutil

for path_name in ["site", "build", "dist"]:
    path = Path(path_name)
    if path.exists():
        shutil.rmtree(path)
        print(f"Removed {path}")
