from json import (loads)
from pathlib import PosixPath as Path
from unittest import TestCase, TestSuite

from config_manager.config_manager2 import ConfigManager, default_config


class TestConfigManager(TestCase):

    # Setup - Start Each Test with CLEAN Config Directory
    @classmethod
    def setUp(self) -> None:
        if Path.home().joinpath('.bw_cfgmgr', '.config').exists():
            Path.home().joinpath('.bw_cfgmgr', '.config').unlink()
            Path.home().joinpath('.bw_cfgmgr').rmdir()
        self.user_conf = {
            "config_dir": "ConfigManagerTestDir",
            "config_file": "ConfigManagerTestDir/cm_conf",
            "application_property_0": "application_value_0",
            "application_property_1": "application_value_1",
            "application_property_N": "application_value_N"
        }
        self.defaultConfigManager = ConfigManager()

    @classmethod
    def tearDown(self) -> None:
        config = default_config()
        if Path.home().joinpath(config["config_dir"], config["config_file"]).exists():
            Path.home().joinpath(config["config_dir"], config["config_file"]).unlink()
            Path.home().joinpath(config["config_dir"]).rmdir()

    #
    @classmethod
    def test__init__(self) -> None:
        self.assertIsInstance(self, self.defaultConfigManager, ConfigManager)

    @classmethod
    def test_verify_config(self) -> None:
        self.assertIsInstance(self, self.defaultConfigManager.config, dict)
