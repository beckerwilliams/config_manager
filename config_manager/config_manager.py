#!/usr/bin/env python3
from json import (dumps, loads)
from pathlib import PosixPath as Path

# _path_parameters are those properties that are `Path` objects in runtime
_def_dirname: str = '.bw_cfgmgr'
_def_cfgname: str = '.config'
_default_pre_config: tuple = (
    ('config_dir', _def_dirname),
    ('config_file', '/'.join((_def_dirname, _def_cfgname)))
)


def _path_parameters() -> list:
    return [entry[0] for entry in [entry for entry in _default_pre_config]]


def default_config() -> dict:
    config = dict((name, Path.home().joinpath(value).absolute()) for name, value in _default_pre_config)
    return config


class ConfigManager(object):

    @classmethod
    def __init__(self, config: dict = None) -> None:
        if not config:  # default config
            self.config = default_config()
        else:  # user config
            self.config = config

        # Make sure config_dir exists
        if not self.config["config_dir"].exists():
            # Create Directory and default config
            self.config["config_dir"].mkdir()
            self.save_config()
        else:
            # If config exists, Load it, Otherwise Save it
                self.load_config()

    @classmethod
    def load_config(self, config=None) -> dict:
        if not config:
            config = self.config
        self.config = self.load_config_filter(loads(config["config_file"].read_text()))

    @staticmethod
    def load_config_filter(config) -> dict:
        new_config = {}
        for prop in config:
            if prop in _path_parameters():
                new_config[prop] = Path(config[prop])
            else:
                new_config[prop] = config[prop]
        return new_config

    @classmethod
    def save_config(self, config=None) -> None:
        if not config:
            config = self.config
        # if not config["config_file"].exists():
        #     config["config_file"].touch()
        config["config_file"].write_text(dumps(self.save_config_filter(config)))

    @staticmethod
    def save_config_filter(config: dict) -> dict:
        new_config = {}
        for prop in config:
            if prop in _path_parameters():
                new_config[prop] = str(config[prop])
            else:
                new_config[prop] = config[prop]
        return new_config
