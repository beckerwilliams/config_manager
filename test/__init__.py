from json import (loads)
from pathlib import PosixPath as Path
from unittest import TestCase, mock

from config_manager import default_config
from config_manager import ConfigManager


# from nose.tools import *


# noinspection PyTypeChecker
class TestConfigManager(TestCase):

    # Setup - Start Each Test with CLEAN Config Directory
    @classmethod
    def setUp(cls) -> None:
        # Default Config Manager
        cls.defaultCM = ConfigManager()
        # User Directory
        cls.user_conf = {"config_dir": "ConfigManagerTestDir", "config_file": "cm_conf",
                         "application_property_0": "application_value_0",
                         "application_property_1": "application_value_1",
                         "application_property_N": "application_value_N"}
        cls.userCM = ConfigManager(cls.user_conf)

    @classmethod
    def tearDown(cls) -> None:
        del cls.defaultCM
        del cls.userCM

    @classmethod  #
    def test___init__(cls) -> None:
        cls.assertIsInstance(cls, cls.userCM, ConfigManager)
        cls.assertIsInstance(cls, cls.userCM.config, dict)

    @classmethod  #
    def test_config_required_properties(cls) -> None:
        cls.assertIn(cls, 'config_dir', cls.defaultCM.config)
        cls.assertIn(cls, 'config_file', cls.defaultCM.config)
        cls.assertIn(cls, 'config_dir', cls.userCM.config)
        cls.assertIn(cls, 'config_file', cls.userCM.config)

    @classmethod
    def test_config_required_values_not_none(cls) -> None:
        cls.assertIsNotNone(cls, cls.defaultCM.config['config_dir'])
        cls.assertIsNotNone(cls, cls.defaultCM.config['config_file'])
        cls.assertIsNotNone(cls, cls.userCM.config['config_dir'])
        cls.assertIsNotNone(cls, cls.userCM.config['config_file'])

    @classmethod
    def test_config_file_creation(cls) -> None:
        cls.assertGreaterEqual(cls, cls.defaultCM.config['config_file'].stat().st_size, 8)
        cls.assertTrue(cls, cls.userCM.config['config_file'].exists())

        for conf_file in [cls.userCM.config['config_file'], cls.defaultCM.config['config_file']]:
            user_config = loads(conf_file.read_text())
            cls.assertIn(cls, 'config_dir', user_config)
            cls.assertIn(cls, 'config_file', user_config)
            cls.assertIsInstance(cls, user_config['config_dir'], str)
            cls.assertIsInstance(cls, user_config['config_file'], str)

    @classmethod
    def test_print_config(cls):
        with mock.patch('sys.stdout') as fake_stdout:
            cls.defaultCM.print_config()
            fake_stdout.assert_has_calls([mock.call.write(str(cls.defaultCM.config))])
