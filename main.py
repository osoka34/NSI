import sys
from pathlib import Path

# BASE_DIR = Path(__file__).resolve().parents[2]
# sys.path.append(str(BASE_DIR))
# print(BASE_DIR)

from internal.app import backend_app

"""
This is the entry point of the application.
"""

app = backend_app()

