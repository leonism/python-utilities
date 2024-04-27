import unittest
from unittest.mock import patch, MagicMock
import os
import sys

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))
# Append the parent directory to the system path
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

import files_organizer

class TestFilesOrganizer(unittest.TestCase):

    @patch('files_organizer.os.system')
    def test_check_pip(self, mock_os_system):
        mock_os_system.return_value = 0
        self.assertEqual(files_organizer.check_pip(), "pip")

        mock_os_system.return_value = 1
        self.assertIsNone(files_organizer.check_pip())

    @patch('files_organizer.os.system')
    def test_check_and_install_colorama(self, mock_os_system):
        mock_os_system.return_value = 0
        with patch('builtins.print') as mocked_print:
            files_organizer.check_and_install_colorama()
            mocked_print.assert_called_with("Pip found. Checking for colorama...")

        mock_os_system.return_value = 1
        with patch('builtins.print') as mocked_print:
            files_organizer.check_and_install_colorama()
            mocked_print.assert_called_with("Pip not found. Please install pip first.")

    def test_get_user_input(self):
        with patch('builtins.input', side_effect=['cancel']):
            self.assertIsNone(files_organizer.get_user_input())

        with patch('builtins.input', side_effect=['invalid_path', 'cancel']):
            self.assertIsNone(files_organizer.get_user_input())

        with patch('builtins.input', side_effect=['/valid/path', '3']):
            self.assertIsNone(files_organizer.get_user_input())

        with patch('builtins.input', side_effect=['/valid/path', '1']):
            self.assertEqual(files_organizer.get_user_input(), ('/valid/path', '1'))

    @patch('files_organizer.os')
    @patch('files_organizer.shutil')
    def test_organize_by_extension(self, mock_shutil, mock_os):
        mock_os.listdir.return_value = ['file1.txt', 'file2.jpg']
        files_organizer.organize_by_extension('/test/path')
        mock_shutil.move.assert_called_with('/test/path/file2.jpg', '/test/path/JPG')

    @patch('files_organizer.os')
    @patch('files_organizer.shutil')
    @patch('files_organizer.time')
    def test_organize_by_date(self, mock_time, mock_shutil, mock_os):
        mock_os.listdir.return_value = ['file1.txt']
        mock_os.path.getmtime.return_value = 1647814800  # Mocking modification time to 2022-03-20 12:00:00
        mock_time.localtime.return_value = MagicMock(tm_year=2022, tm_mon=3)  # Mocking localtime to March 2022
        files_organizer.organize_by_date('/test/path')
        mock_shutil.move.assert_called_with('/test/path/file1.txt', '/test/path/2022/3')

if __name__ == '__main__':
    unittest.main()
