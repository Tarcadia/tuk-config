# -*- coding: UTF-8 -*-


__author__ = "Tarcadia"
__url__ = "https://github.com/Tarcadia/tuk-config"
__copyright__ = "Copyright 2025"
__credits__ = ["Tarcadia"]
__license__ = "MIT"
__version__ = "0.2.0"


from ._config import Config
from ._config import CONFIG_META_SECTION
from ._config import CONFIG_META_SECTION_INCLUDE
from ._path import CURRENT_MACHINE_DIR
from ._path import CURRENT_USER_DIR
from ._path import CURRENT_APP_PATH
from ._path import CURRENT_APP_DIR
from ._path import CURRENT_WORKING_DIR
from ._default import CONFIG

__all__ = [
    "Config",
    "CONFIG_META_SECTION",
    "CONFIG_META_SECTION_INCLUDE",
    "CURRENT_MACHINE_DIR",
    "CURRENT_USER_DIR",
    "CURRENT_APP_PATH",
    "CURRENT_APP_DIR",
    "CURRENT_WORKING_DIR",
    "CONFIG"
]

