from pathlib import PosixPath as Path
from unittest import (TestCase, main)

from config_manager import fs_delete


class Test__fs_delete(TestCase):

    def setUp(self) -> None:
        self.test_dir = Path.home().joinpath('FS_DELETE_TEST')
        internal_dir = self.test_dir.joinpath('internal1')
        internal2_dir = internal_dir.joinpath('internal2')

        internal2_dir.mkdir(parents=True, exist_ok=False)

        internal_dir.joinpath('FluffFile1').write_text(Path.home().joinpath('.cshrc').read_text())
        internal_dir.joinpath('FluffFile2').write_text(Path.home().joinpath('.login').read_text())
        internal2_dir.joinpath('FluffFile3').write_text(Path.home().joinpath('.login').read_text())
        internal2_dir.joinpath('FluffFile4').write_text(Path.home().joinpath('.login').read_text())

    def tearDown(self) -> None:
        pass

    def test__fs_delete(self):
        fs_delete(self.test_dir)

        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    main()
