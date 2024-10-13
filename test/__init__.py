from json import (loads)
from unittest import (TestCase, mock)
from pathlib import PosixPath as Path

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
        cls.defaultCM = ConfigManager(config=user_config, root_dir=user_root)

    @classmethod
    def tearDown(cls) -> None:
        del cls.defaultCM

    @classmethod  #
    def test___init__(cls) -> None:
        cls.assertIsInstance(cls, cls.defaultCM, ConfigManager)
        cls.assertIsInstance(cls, cls.defaultCM.config, dict)

    @classmethod  #
    def test_config_required_properties(cls) -> None:
        cls.assertIn(cls, 'config_dir', cls.defaultCM.config)
        cls.assertIn(cls, 'config_file', cls.defaultCM.config)

    @classmethod
    def test_config_required_values_not_none(cls) -> None:
        cls.assertIsNotNone(cls, cls.defaultCM.config['config_dir'])
        cls.assertIsNotNone(cls, cls.defaultCM.config['config_file'])

    @classmethod
    def test_print_config(cls):
        with mock.patch('sys.stdout') as fake_stdout:
            cls.defaultCM.print_config()
            fake_stdout.assert_has_calls([mock.call.write(str(cls.defaultCM.config))])

    @classmethod
    def test_config_file_creation(cls) -> None:
        cls.assertTrue(cls.defaultCM.config['config_file'].exists(),
                       f'Config File: {cls.defaultCM.config['config_file']} does not exist')
        cls.assertGreater(cls, cls.defaultCM.config['config_file'].stat().st_size, 1)

        for conf_file in [cls.defaultCM.config['config_file']]:
            user_config = loads(conf_file.read_text())
            cls.assertIn(cls, 'config_dir', user_config)
            cls.assertIn(cls, 'config_file', user_config)
            cls.assertIsInstance(cls, user_config['config_dir'], str)
            cls.assertIsInstance(cls, user_config['config_file'], str)

    @classmethod
    def test__disable_path_properties(cls) -> None:
        clean_config = _disable_path_properties(cls.defaultCM.config)
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
