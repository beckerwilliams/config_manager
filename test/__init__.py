from pathlib import PosixPath as Path
from unittest import (TestCase, mock)

from config_manager import (ConfigManager, _disable_path_properties, _enable_path_properties, default_config)


# noinspection PyTypeChecker
class TestConfigManager(TestCase):

    # Setup - Start Each Test with CLEAN Config Directory
    @classmethod
    def setUp(cls) -> None:
        user_config = default_config()
        user_config['extr_attr1'] = 'extr_attr1'
        user_config['extr_attr2'] = 'extr_attr2'
        user_config['extr_attr3'] = 'extr_attr3'
        user_root = Path.home().joinpath('CM_TEST_ROOT')
        cls.userCM = ConfigManager(None, user_root)
        cls.defaultCM = ConfigManager()

    @classmethod
    def tearDown(cls) -> None:
        del cls.defaultCM
        # pass

    @classmethod
    def test___init__(cls) -> None:
        cls.assertIsInstance(cls, cls.defaultCM, ConfigManager)
        cls.assertIsInstance(cls, cls.defaultCM.config, dict)
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
    def test_print_config(cls):
        with mock.patch('sys.stdout') as fake_stdout:
            cls.defaultCM.print_config()
            fake_stdout.assert_has_calls([mock.call.write(str(cls.defaultCM.config))])

        with mock.patch('sys.stdout') as fake_stdout:
            cls.userCM.print_config()
            fake_stdout.assert_has_calls([mock.call.write(str(cls.userCM.config))])

    @classmethod
    def test_config_file_creation(cls) -> None:
        # Default (No Config, No root_dir
        cls.assertTrue(cls.defaultCM.config['config_file'].exists(),
                       f'Config File: {cls.defaultCM.config['config_file']} does not exist')
        cls.assertIsInstance(cls, cls.defaultCM.config['config_file'], Path)
        # print(f'defaultCM Config File: {cls.defaultCM.config['config_file']}')
        cls.assertTrue(cls.defaultCM.config['config_file'].stat().st_size > 1, f'On Disk File Stat Failed')
        # w/ User Config, Non-Default Root Dir
        cls.assertTrue(cls.userCM.config['config_file'].exists(),
                       f'Config File: {cls.userCM.config['config_file']} does not exist')
        cls.assertIsInstance(cls, cls.userCM.config['config_file'], Path)
        # print(f'defaultCM Config File: {cls.defaultCM.config['config_file']}')
        cls.assertTrue(cls.userCM.config['config_file'].stat().st_size > 1, f'On Disk File Stat Failed')

    @classmethod
    def test__disable_path_properties(cls) -> None:
        clean_config = _disable_path_properties(cls.defaultCM.config)
        cls.assertIsInstance(cls, clean_config['config_dir'], str, "_disable_path_properties() FAILED")
        cls.assertIsInstance(cls, clean_config['config_file'], str, "_disable_path_properties() FAILED")
        cls.assertTrue(clean_config['config_dir'] == default_config()['config_dir'], f'Failed')
        cls.assertTrue(clean_config['config_file'] == default_config()['config_file'], f'Failed')

        clean_config = _disable_path_properties(cls.userCM.config)
        cls.assertIsInstance(cls, clean_config['config_dir'], str, "_disable_path_properties() FAILED")
        cls.assertIsInstance(cls, clean_config['config_file'], str, "_disable_path_properties() FAILED")
        cls.assertTrue(clean_config['config_dir'] == default_config()['config_dir'], f'Failed')
        cls.assertTrue(clean_config['config_file'] == default_config()['config_file'], f'Failed')

    @classmethod
    def test__enable_path_properties(cls) -> None:
        mapped_config = _enable_path_properties(cls.defaultCM.config)
        cls.assertIsInstance(cls, mapped_config['config_dir'], Path, "_disable_path_properties() FAILED")
        cls.assertIsInstance(cls, mapped_config['config_file'], Path, "_disable_path_properties() FAILED")
        cls.assertTrue(mapped_config['config_dir'] == default_config()['config_dir'], f'Failed')
        cls.assertTrue(mapped_config['config_file'] == default_config()['config_file'], f'Failed')

        mapped_config = _enable_path_properties(cls.userCM.config)
        cls.assertIsInstance(cls, mapped_config['config_dir'], Path, "_disable_path_properties() FAILED")
        cls.assertIsInstance(cls, mapped_config['config_file'], Path, "_disable_path_properties() FAILED")
        cls.assertTrue(mapped_config['config_dir'] == default_config()['config_dir'], f'Failed')
        cls.assertTrue(mapped_config['config_file'] == default_config()['config_file'], f'Failed')

