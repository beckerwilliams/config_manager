from json import (loads)
from pathlib import PosixPath as Path
from unittest import TestCase

from config_manager.config_manager import ConfigManager, default_config


class TestConfigManager(TestCase):

    # Setup - Start Each Test with CLEAN Config Directory
    @classmethod
    def setUp(self) -> None:
        self.user_conf = {
            "config_dir": Path.home().joinpath("ConfigManagerTestDir"),
            "config_file": Path.home().joinpath("ConfigManagerTestDir","cm_conf"),
            "application_property_0": "application_value_0",
            "application_property_1": "application_value_1",
            "application_property_N": "application_value_N"
        }
        self.userConfigManager = ConfigManager(self.user_conf)
        self.defaultConfigManager = ConfigManager()

    @classmethod
    def tearDown(self) -> None:
        if self.defaultConfigManager.config["config_file"].exists():
            self.defaultConfigManager.config["config_file"].unlink()
        if self.defaultConfigManager.config["config_dir"].exists():
            self.defaultConfigManager.config["config_dir"].rmdir()

        del self.defaultConfigManager

    def test_default_config(self):
        print(default_config())
        self.assertIsNotNone(default_config())

    # Need Two Additional Test Cases for coverage,
    # 1. Where 'self.config["config_file].exists() is FALSE
    # 2. Where the CONFIG saved has ADD'L Properties (besides `dir` and `file`)
    def test_config_file_DOESNT_EXIST(self):
        pass
        self.defaultConfigManager.config["config_file"].unlink()
        self.assertIsNotNone(self.defaultConfigManager.config["config_file"])




    # @classmethod
    # def test_init_default(self):
    #     self.assertIsNotNone(self.defaultConfigManager, True)
    #     self.assertTrue(self.defaultConfigManager.config["config_dir"].exists())
    #     self.assertTrue(self.defaultConfigManager.config["config_file"].exists())
    #     print(f'{self.defaultConfigManager.config}')
    #
    # @classmethod
    # def test_init_user_conf(self):
    #     self.assertIsNotNone(self.userConfigManager)



