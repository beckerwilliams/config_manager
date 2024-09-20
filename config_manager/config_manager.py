#!/usr/bin/env python3
from json import (dumps, loads)
from pathlib import PosixPath as Path

# _path_parameters are those properties that are `Path` objects in runtime
_path_parameters = ('config_dir', 'config_file')


def default_config():
    dconf = {
        "config_dir": Path.home().joinpath(".bw_config_manager"),
        "config_file": Path.home().joinpath(".bw_config_manager","config"),
    }
    return dconf


class ConfigManager(object):

    @classmethod
    def __init__(self, config=None) -> None:
        if not config:
            self.config = default_config()
        else:
            self.config = config
        # Save Config if None Exists
        if not self.config["config_dir"].exists():
            self.config["config_dir"].mkdir()
        self.save_config()

    @classmethod
    def load_config(self, config=None) -> dict:
        if not config:
            config = self.config
        return self.load_config_filter(loads(self.config["config_file"].read_text()))

    @staticmethod
    def load_config_filter(config) -> dict:
        new_config = {}
        for prop in config:
            if prop in _path_parameters:
                new_config[prop] = Path(config[prop])
            else:
                new_config[prop] = config[prop]
        return new_config

    @classmethod
    def save_config(self, config=None) -> None:
        if not config:
            config = self.config
        # if not config["config_dir"].exists():
        #     config["config_dir"].mkdir()
        if not config["config_file"].exists():
            config["config_file"].touch()

        config["config_file"].write_text(dumps(self.save_config_filter(config)))

    @staticmethod
    def save_config_filter(config: dict) -> dict:
        # We DO NOT USE self.config | We
        new_config = {}
        for prop in config:
            if prop in _path_parameters:
                new_config[prop] = str(config[prop])
            else:
                new_config[prop] = config[prop]
        return new_config

    def default_config(self):
        return default_config()
