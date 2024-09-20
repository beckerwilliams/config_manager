from json import (loads)
from pathlib import PosixPath as Path
from unittest import TestCase

from config_manager.config_manager import ConfigManager, default_config


class TestConfigManager(TestCase):

    # Setup - Start Each Test with CLEAN Config Directory
    def setUp(self) -> None:
        self.tcm = ConfigManager()
        self.test_conf = {
            "config_dir": Path.home().joinpath("ConfigManagerTestDir"),
            "config_file": Path.home().joinpath("ConfigManagerTestDir","cm_conf"),
            "application_property_0": "application_value_0",
            "application_property_1": "application_value_1",
            "application_property_N": "application_value_N"
        }

    def tearDown(self) -> None:
        if self.tcm.config["config_file"].exists():
            self.tcm.config["config_file"].unlink()
        if self.tcm.config["config_dir"].exists():
            self.tcm.config["config_dir"].rmdir()

        del self.tcm

    def test_init(self):
        self.assertIsNotNone(self.tcm, True)
        self.assertDictEqual(self.tcm.config, default_config())
        self.assertTrue(self.tcm.config["config_dir"].exists())
        self.assertTrue(self.tcm.config["config_file"].exists())
        self.assertTrue('config_file' in self.tcm.config)
        self.assertTrue('config_dir' in self.tcm.config)

    def test_load_configuration_defaultconfig(self):
        self.assertDictEqual(
            self.tcm.load_config(loads(self.tcm.config["config_file"].read_text())),
            default_config())

    def test_load_configuration_testconfig(self):
        cm = ConfigManager(config=self.test_conf)
        default_props = default_config()
        for prop in default_config():
            self.assertTrue(prop in default_props)
        test_config = cm.load_config(self.test_conf)
        self.assertDictEqual(test_config, self.test_conf)


    def test_load_configuration_emptyconfig(self):
        cm = ConfigManager()
        self.assertDictEqual(
            cm.load_config(config=None),
            default_config())

    def test_default_config(self):
        self.assertEqual(self.tcm.default_config(), default_config())

    def test_save_configuration(self):
        pass
