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
        """
        If no config provided, default is assigned as `self.config`
        If a Configuration File corresponding to provided or default config exists,
        it will take precedence over the provided configuration dict.

        :param config: Application Configruation Directory and File
        :type config: dict
        """
        if not config:
            config = default_config()

        config_file = Path.home().joinpath(config["config_dir"], config["config_file"])
        if config_file.exists and config_file.is_file():
            self.config = _enable_path_properties(loads(config_file.read_text()))
        else:
            self.config = _enable_path_properties(default_config())
            if not Path.home().joinpath(config["config_dir"]).exists():
                Path.home().joinpath(config["config_dir"]).mkdir(exist_ok=True)
            Path.home().joinpath(config["config_dir"], config["config_file"]).write_text(dumps(config))

