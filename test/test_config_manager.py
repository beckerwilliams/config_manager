from json import (loads)
from pathlib import PosixPath as Path
from unittest import TestCase, main

from config_manager.config_manager import ConfigManager, default_config


# # SETUP - Eliminate Existing Configuration File and Directory
# if default_config.get("config_file").exists():
#     default_config["config_file"].unlink()
#
# if default_config.get("config_dir").exists():
#     default_config["config_dir"].rmdir()


class TestConfigManager(TestCase):

    # Setup - Start Each Test with CLEAN Config Directory
    def setUp(self) -> None:
        self.tcm = ConfigManager()
        self.test_conf = {
            "config_dir": Path.home().joinpath("ConfigManagerTestDir"),
            "config_file": Path.home().joinpath("cm_conf"),
        }

    def tearDown(self) -> None:
        if self.tcm.config["config_file"].exists():
            self.tcm.config["config_file"].unlink()
        if self.tcm.config["config_dir"].exists():
            self.tcm.config["config_dir"].rmdir()

        if self.tcm.config["config_dir"].exists():
            self.tcm.config["config_dir"].rmdir()
        if self.tcm.config["config_file"].exists():
            self.tcm.config["config_file"].unlink()
        del self.tcm

    def test_init(self):
        self.assertIsNotNone(self.tcm, True)

    def test_config_equals_default(self):
        self.assertDictEqual(self.tcm.config, default_config())  # dd assertion here

    def test_config_dir_exists(self):
        self.assertTrue(self.tcm.config["config_dir"].exists())

    def test_config_file_exists(self):
        self.assertTrue(self.tcm.config["config_file"].exists())

    def test_load_configuration_defaultconfig(self):
        self.assertDictEqual(
            self.tcm.load_config_filter(loads(self.tcm.config["config_file"].read_text())),
            default_config())

    def test_load_configuration_testconfig(self):
        cm = ConfigManager(config=self.test_conf)
        self.assertDictEqual(
            cm.load_config_filter(loads(cm.config["config_file"].read_text())),
            self.test_conf)

    def test_save_configuration(self):
        pass


if __name__ == '__main__':
    main()
