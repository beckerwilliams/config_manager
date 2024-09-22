#!/usr/bin/env python3
from json import (dumps, loads)
from pathlib import PosixPath as Path

# _path_parameters are those properties that are `Path` objects in runtime
_def_dirname: str = '.bw_cfg'
_def_cfgname: str = '.config'

# ________________________________________ (DO NOT MODIFY BELOW) _________________________________
_default_pre_config: tuple = (
    ('config_dir', _def_dirname),
    ('config_file', _def_cfgname))


def _path_parameters() -> list:
    """

    :return: names of configuration properties to be treated as paths
    :rtype: list
    """
    return [entry[0] for entry in [entry for entry in _default_pre_config]]


def _enable_path_properties(config: dict) -> dict:
    for prop in config:
        if prop in _path_parameters():
            config[prop] = Path(config[prop])
    return config

def _disable_path_properties(config: dict) -> dict:
    for prop in config:
        if prop in _path_parameters():
            config[prop] = config

def default_config() -> dict:
    """

    :return: JSON Object (No PATH Parameters as Values)
    :rtype: dict
    """
    return dict((name, value) for name, value in _default_pre_config)


class ConfigManager(object):

    @classmethod
    def __init__(self, config: dict = None) -> None:
        if config:
            config = _enable_path_properties(config)
        else:
            config = _enable_path_properties(default_config())
        self.config = config  # Delete This Line when CoMPLETE BELOW tbd