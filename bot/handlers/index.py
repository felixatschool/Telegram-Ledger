"""
index.py
---------
index all function handlers
"""


# imports here -----------------------
from .help import help_command
from .report import report
from .buy import buy
from .transfer import transfer
from .admin import admin
from .logger import log

command_map = {
    'report' : report,
    'buy' : buy,
    'transfer' : transfer,
    'admin' : admin,
    'help' : help_command
    }

# --------------------------------------
def index():
    """
    
    """
    return command_map
