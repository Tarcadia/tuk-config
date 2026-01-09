# -*- coding: UTF-8 -*-


import logging

from pathlib import Path

from ._config import Config
from ._config import CONFIG_META_SECTION
from ._config import CONFIG_META_SECTION_INCLUDE
from ._path import CURRENT_MACHINE_DIR
from ._path import CURRENT_USER_DIR
from ._path import CURRENT_APP_DIR
from ._path import CURRENT_WORKING_DIR



def CONFIG(name:str|Path) -> Config:
    _paths = [
        (_p / name)
        for _p in [
            CURRENT_WORKING_DIR,
            CURRENT_APP_DIR,
            CURRENT_USER_DIR,
            CURRENT_MACHINE_DIR
        ]
        if _p is not None
        if (_p / name).exists()
    ]
    
    _config = Config()

    for _i, _path in enumerate(_paths):
        _c = Config(_path)
        _config.join(_c)
        _npath = _paths[_i + 1] if _i + 1 < len(_paths) else None
        _include = _c.get(CONFIG_META_SECTION, CONFIG_META_SECTION_INCLUDE, fallback=_npath)
        if _include and _npath and Path(_include).resolve() == _npath.resolve():
            continue
        elif _include:
            while _include:
                _c = Config(_include)
                _config.join(_c)
                _include = _c.get(CONFIG_META_SECTION, CONFIG_META_SECTION_INCLUDE, fallback=None)
            break
        elif not _include:
            break

    return _config
