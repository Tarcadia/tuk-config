# -*- coding: UTF-8 -*-


import logging

import platform
import os
import sys
from pathlib import Path



# OS based Machine and User config path
if platform.system() == "Windows":
    _MACHINE_PATH   = os.environ.get("ALLUSERSPROFILE", None)
    _USER_PATH      = os.environ.get("USERPROFILE", None)
elif platform.system() in ["Linux", "Darwin"]:
    _MACHINE_PATH   = "/etc" if os.path.exists("/etc") else None
    _USER_PATH      = os.environ.get("HOME", None)
else:
    _MACHINE_PATH   = None
    _USER_PATH      = None


# Application based binary path and temp path
if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    _APP_PATH       = sys.executable
    _APP_TMP        = sys._MEIPASS
elif (__main__ := sys.modules["__main__"]) and hasattr(__main__, "__file__"):
    _APP_PATH       = os.path.abspath(__main__.__file__)
    _APP_TMP        = None
else:
    _APP_PATH       = None
    _APP_TMP        = None


CURRENT_MACHINE_DIR = _MACHINE_PATH and Path(_MACHINE_PATH)
CURRENT_USER_DIR    = _USER_PATH and Path(_USER_PATH)
CURRENT_APP_PATH    = _APP_PATH and Path(_APP_PATH)
CURRENT_APP_DIR     = CURRENT_APP_PATH.parent if CURRENT_APP_PATH else None
CURRENT_WORKING_DIR = Path(os.getcwd())

